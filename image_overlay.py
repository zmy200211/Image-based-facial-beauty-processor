import cv2 as cv
import numpy as np

'''
函数：add_alpha_channel
参数：
image：jpg原图像
功能：为jpg图像添加alpha通道
'''


def add_alpha_channel_424(image):
    # 判断图片是否为4通道
    if image.shape[2] == 4:
        return image
    # 剥离jpg图像通道
    b, g, r = cv.split(image)
    # 创建alpha通道，255表示不透明
    alpha_channel = np.ones(b.shape, dtype=b.dtype) * 255
    # 融合通道
    new_image = cv.merge((b, g, r, alpha_channel))
    return new_image


'''
函数：merge_jpg_and_png
参数：
jpg：jpg图像
png：png透明图像
ratio：png透明程度 [0 ~ 1][浅~深]
功能：将jpg图像与png图像叠加
'''


def merge_jpg_and_png_424(jpg, png, ratio):
    # png图像左上角和右下角的坐标
    x2 = png.shape[1]
    y2 = png.shape[0]
    alpha_png = np.ones((y2, x2))
    alpha_jpg = np.ones((y2, x2))
    # 获取要覆盖图像的alpha值比例
    for y in range(y2):
        for x in range(x2):
            alpha_png[y, x] = png[y, x, 3] / 255 * ratio
            alpha_jpg[y, x] = 1 - alpha_png[y, x]
    # 开始叠加
    for y in range(y2):
        for x in range(x2):
            for c in range(4):
                jpg[y, x, c] = ((alpha_jpg[y, x] * jpg[y, x, c]) + (alpha_png[y, x] * png[y, x, c]))
    return jpg


if __name__ == '__main__':
    png_img = cv.imread("mask_blush/mask_blush_right.png", -1)
    print(png_img[0, 0, 0], png_img[0, 0, 1], png_img[0, 0, 2], png_img[0, 0, 3])
    jpg_img = cv.imread("test_image/one_face.jpg")
    jpg_img = add_alpha_channel_424(jpg_img)
    jpg_img = merge_jpg_and_png_424(jpg_img, png_img, 0.5)
    cv.imwrite("2.png", jpg_img)





