import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from numpy import clip

from face_detect import face_detect_424

'''
函数：LE
参数：
scr_image：原始彩图
image：原始灰度图像
center：单眼中心位置
radius：大眼区域半径
intensity：大眼程度
功能：实现”液化-膨胀“算法
'''


def LE_424(scr_image, image, center, radius, intensity):
    # 图像大小
    height, width = image.shape
    # 计算大眼区域
    x = clip(center[0] - radius, 0, width - 1)
    y = clip(center[1] - radius, 0, height - 1)
    w = clip(center[0] + radius, 0, width - 1)
    h = clip(center[1] + radius, 0, height - 1)
    # 计算大眼区域半径的平方
    D = pow(radius, 2)
    k0 = intensity / 100.0
    # 初始化映射后(x, y)对应原图的列、行坐标矩阵
    map_x = np.array([[i for i in range(width)] for j in range(height)], dtype=np.float32)
    map_y = np.array([[j for i in range(width)] for j in range(height)], dtype=np.float32)
    # 遍历大眼区域的每个像素
    for j in range(int(y), int(h)):
        for i in range(int(x), int(w)):
            # 计算当前处理点到中心点的欧氏距离的平方
            dis = pow(i - center[0], 2) + pow(j - center[1], 2)
            # 若当前处理点位置未超过大眼区域的范围
            if dis < D:
                # 计算缩放比例因子
                k = 1.0 - (1.0 - dis / D) * k0
                # 计算当前处理点大眼后的位置
                px = clip((i - center[0]) * k + center[0], 0, width - 1)
                py = clip((j - center[1]) * k + center[1], 0, height - 1)
                map_x[j, i] = px
                map_y[j, i] = py
    # 通道拆分
    blue, green, red = cv.split(scr_image)
    # 分别计算，使用双线性插值
    big_image_b = cv.remap(blue, map_x, map_y, interpolation=cv.INTER_LINEAR)
    big_image_g = cv.remap(green, map_x, map_y, interpolation=cv.INTER_LINEAR)
    big_image_r = cv.remap(red, map_x, map_y, interpolation=cv.INTER_LINEAR)
    # 通道合成
    big_image = cv.merge([big_image_b, big_image_g, big_image_r])
    return big_image


'''
函数：auto_big_eyes
参数：
scr_image：原始彩图
image：原始灰度图像
faces：所有人脸的位置
all_face_points：所有人脸五官的位置
intensity：大眼程度
功能：自动大眼
'''


def auto_big_eyes_424(scr_image, image, faces, all_face_points, intensity):
    # 遍历所有人脸
    for people in range(len(faces)):
        # 获得一张人脸框位置
        face = faces[people]
        # 获得一张脸的关键点位置
        face_points = all_face_points[people]
        # 左眼中心点位置
        cen_x_left = (face_points.part(37).x + face_points.part(38).x) / 2
        cen_y_left = (face_points.part(37).y + face_points.part(41).y) / 2
        cen_left = (cen_x_left, cen_y_left)
        # 右眼中心点位置
        cen_x_right = (face_points.part(43).x + face_points.part(44).x) / 2
        cen_y_right = (face_points.part(43).y + face_points.part(47).y) / 2
        cen_right = (cen_x_right, cen_y_right)
        # 左眼半径
        dis_left = pow(pow(face_points.part(36).x - face_points.part(39).x, 2) +
                       pow(face_points.part(36).y - face_points.part(39).y, 2), 0.5)
        # 右眼半径
        dis_right = pow(pow(face_points.part(42).x - face_points.part(45).x, 2) +
                        pow(face_points.part(42).y - face_points.part(45).y, 2), 0.5)
        # 大眼区域半径
        if dis_left >= dis_right:
            radius = dis_left
        else:
            radius = dis_right
        # 处理左眼
        scr_image = LE_424(scr_image, image, cen_left, radius, intensity)
        image = cv.cvtColor(scr_image, cv.COLOR_BGR2GRAY)
        # 处理右眼
        scr_image = LE_424(scr_image, image, cen_right, radius, intensity)
        image = cv.cvtColor(scr_image, cv.COLOR_BGR2GRAY)
    return scr_image


'''
函数：start_auto_big_eyes
参数：
scr_image：原始彩色图像
intensity：瘦脸程度（范围[-50 ~ 50]，负值为小眼，正值为大眼）
功能：启动自动大眼功能
'''


def start_auto_big_eyes_424(scr_image, intensity):
    # 转灰度图
    gray_image = cv.cvtColor(scr_image, cv.COLOR_BGR2GRAY)
    faces, all_shape = face_detect_424(gray_image)
    lift_image = auto_big_eyes_424(scr_image, gray_image, faces, all_shape, intensity)
    return lift_image


if __name__ == '__main__':
    img = cv.imread("tow_face.jpg")
    result = start_auto_big_eyes_424(img, 10)
    plt.subplot(121), plt.imshow(img[:, :, [2, 1, 0]]), plt.title('input')
    plt.subplot(122), plt.imshow(result[:, :, [2, 1, 0]]), plt.title('output')
    plt.show()
