import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from numpy import clip
from face_detect import face_detect_424

'''
函数：IDW
参数：
scr_image：原始彩图
image：原始灰度图像
input_points：输入控制点位置列表
output_points：输出控制点位置列表
功能：实现图像反距离加权（IDW）插值变形算法
'''


def IDW_424(scr_image, image, input_points, output_points):
    u = 1
    # 人脸图像的高、宽
    height, width = image.shape
    # 初始化映射后(x, y)对应原图的列、行坐标矩阵
    map_x = np.array([[i for i in range(width)] for j in range(height)], dtype=np.float32)
    map_y = np.array([[j for i in range(width)] for j in range(height)], dtype=np.float32)
    # 遍历人脸图像中的每一个像素位置
    for j in range(height):
        for i in range(width):
            x = 0
            y = 0
            sum_w = 0
            # 遍历输入控制点像素位置
            for k in range(len(input_points)):
                # 获取当前处理控制点的位置
                input_point = input_points[k]
                output_point = output_points[k]
                # (i, j)若是控制点
                if (i == input_point[0]) and (j == input_point[1]):
                    w = 1.0
                else:
                    v = 1.0 / pow(pow(i - input_point[0], 2) + pow(j - input_point[1], 2), u)
                    w = v
                sum_w += w
                x += w * (output_point[0] + i - input_point[0])
                y += w * (output_point[1] + j - input_point[1])
            x = x / sum_w
            y = y / sum_w
            # 将x, y控制在图像大小范围内
            x = clip(x, 0, width - 1)
            y = clip(y, 0, height - 1)
            map_x[j, i] = x
            map_y[j, i] = y
    # 通道拆分
    blue, green, red = cv.split(scr_image)
    # 分别计算
    lift_image_b = cv.remap(blue, map_x, map_y, interpolation=cv.INTER_LINEAR)
    lift_image_g = cv.remap(green, map_x, map_y, interpolation=cv.INTER_LINEAR)
    lift_image_r = cv.remap(red, map_x, map_y, interpolation=cv.INTER_LINEAR)
    # 通道合成
    lift_image = cv.merge([lift_image_b, lift_image_g, lift_image_r])
    return lift_image


'''
函数：auto_face_lift
参数：
scr_image：原始彩图
image：原始灰度图像
faces：所有人脸的位置
all_face_points：所有人脸五官的位置
intensity：瘦脸程度
功能：自动瘦脸
'''


def auto_face_lift_424(scr_image, image, faces, all_face_points, intensity):
    # 遍历所有人脸
    for people in range(len(faces)):
        # 获得一张人脸框位置
        face = faces[people]
        # 获得一张脸的关键点位置
        face_points = all_face_points[people]
        # 获得9个输出控制点位置和一个中心点位置
        p5 = (face_points.part(0).x, face_points.part(0).y)
        p6 = (face_points.part(4).x, face_points.part(4).y)
        p7 = (face_points.part(8).x, face_points.part(8).y)
        p8 = (face_points.part(12).x, face_points.part(12).y)
        p9 = (face_points.part(16).x, face_points.part(16).y)
        p0 = (face_points.part(29).x, face_points.part(29).y)
        # 计算瘦脸后p6和p8的位置，K为偏移程度
        K = 0.1 * intensity / 100
        p61 = (p6[0] + (p0[0] - p6[0]) * K, p6[1] + (p0[1] - p6[1]) * K)
        p81 = (p8[0] + (p0[0] - p8[0]) * K, p8[1] + (p0[1] - p8[1]) * K)
        # 计算人脸框四个点的位置
        min_x = face.left()
        min_y = face.top()
        max_x = face.right()
        max_y = face.bottom()
        # 输入控制点
        input_points = [(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y),
                        p5, p6, p7, p8, p9]
        # 输出控制点
        output_points = [(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y),
                         p5, p61, p7, p81, p9]
        # 有多张人脸的情况
        scr_image = IDW_424(scr_image, image, input_points, output_points)
        image = cv.cvtColor(scr_image, cv.COLOR_BGR2GRAY)
    return scr_image


'''
函数：start_auto_face_lift
参数：
scr_image：原始彩色图像
intensity：瘦脸程度（范围[-50 ~ 50]，负值为瘦脸，正值为胖脸）
功能：启动自动瘦脸功能
'''


def start_auto_face_lift_424(scr_image, intensity):
    # 转灰度图
    gray_image = cv.cvtColor(scr_image, cv.COLOR_BGR2GRAY)
    faces, all_shape = face_detect_424(gray_image)
    lift_image = auto_face_lift_424(scr_image, gray_image, faces, all_shape, intensity)
    return lift_image


if __name__ == '__main__':
    img = cv.imread("one_face.jpg")
    result = start_auto_face_lift_424(img, -50)
    plt.subplot(121), plt.imshow(img[:, :, [2, 1, 0]]), plt.title('input')
    plt.subplot(122), plt.imshow(result[:, :, [2, 1, 0]]), plt.title('output')
    plt.show()
