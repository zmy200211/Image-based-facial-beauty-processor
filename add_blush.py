import cv2
from matplotlib import pyplot as plt
<<<<<<< HEAD

=======
>>>>>>> 3eb85d509c3ae985826701308b81c0e535836380
from image_overlay import *
from face_detect import *

'''
函数：make_base_424
参数：
scr_image：处理图像
msk_image：红腮图片
input_points：原点位
transformation_points：放射变换后的点位
ration：腮红透明度[0~1][透明~不透明]
功能：添加一个腮红
'''


def make_base_424(src_image, msk_image, input_points, transformation_points, ration):
    # 计算仿射变换矩阵
    A = cv2.getAffineTransform(input_points, transformation_points)
    # 将腮红图像进行仿射变换，使用双线性插值
    png = cv2.warpAffine(msk_image, A, (src_image.shape[1], src_image.shape[0]), flags=cv2.INTER_LINEAR)
<<<<<<< HEAD
    cv2.imwrite("aaa.png", png)
=======
>>>>>>> 3eb85d509c3ae985826701308b81c0e535836380
    # 将原图与腮红叠加
    src_image = add_alpha_channel_424(src_image)
    src_image = merge_jpg_and_png_424(src_image, png, ration)
    return src_image


def face_blush_424(src_image, faces, all_face_points, ratio):
    # 读取腮红图片
    left_blush = cv2.imread("mask_blush/mask_blush_left.png", -1)
    right_blush = cv2.imread("mask_blush/mask_blush_right.png", -1)
    # 腮红变换前的位置
    left_points = np.float32([[163, 219], [222, 327], [246, 238]])
    right_points = np.float32([[356, 219], [297, 327], [274, 238]])
    # 遍历所有人脸
    for people in range(len(faces)):
        # 获得一张脸的关键点位置
        face_points = all_face_points[people]
        # 左脸颊三点位置
        p1_left = [face_points.part(0).x, face_points.part(0).y]
        p2_left = [face_points.part(5).x, face_points.part(5).y]
        p3 = [face_points.part(29).x, face_points.part(29).y]
        # 右脸颊三点位置
        p1_right = [face_points.part(16).x, face_points.part(16).y]
        p2_right = [face_points.part(11).x, face_points.part(11).y]
        # 给左脸颊加腮红
        output_points = np.float32([p1_left, p2_left, p3])
        src_image = make_base_424(src_image, left_blush, left_points, output_points, ratio)
        # 给右脸颊加腮红
        output_points = np.float32([p1_right, p2_right, p3])
        src_image = make_base_424(src_image, right_blush, right_points, output_points, ratio)
    return src_image


def start_add_blush_424(src_image, ratio):
    # 转灰度图
    gray_image = cv.cvtColor(src_image, cv.COLOR_BGR2GRAY)
    faces, all_shape = face_detect_424(gray_image)
    blush = face_blush_424(src_image, faces, all_shape, ratio)
    return blush


if __name__ == '__main__':
    img = cv.imread("tow_face.jpg")
    result = start_add_blush_424(img, 0.3)
    plt.subplot(121), plt.imshow(img[:, :, [2, 1, 0]]), plt.title('input')
    plt.subplot(122), plt.imshow(result[:, :, [2, 1, 0]]), plt.title('output')
    plt.show()
