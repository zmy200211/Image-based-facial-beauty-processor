# -*- coding: utf-8 -*-
"""
Created on 2023年5月30日
@author 许梦媛
<<<<<<< HEAD
@description: 本程序通过图层混合实现对人脸美白
@version 2.0
=======
@description: 本程序通过颜色查找表实现对人脸美白
@version 1.0
>>>>>>> 3eb85d509c3ae985826701308b81c0e535836380
@CopyRight: CQUT
"""
from PIL import Image
import cv2
from PIL import ImageEnhance
import numpy

<<<<<<< HEAD
=======
Color_list = [
    1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 31, 33, 35, 37, 39,
    41, 43, 44, 46, 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 66, 67, 69, 71, 73, 74,
    76, 78, 79, 81, 83, 84, 86, 87, 89, 91, 92, 94, 95, 97, 99, 100, 102, 103, 105,
    106, 108, 109, 111, 112, 114, 115, 117, 118, 120, 121, 123, 124, 126, 127, 128,
    130, 131, 133, 134, 135, 137, 138, 139, 141, 142, 143, 145, 146, 147, 149, 150,
    151, 153, 154, 155, 156, 158, 159, 160, 161, 162, 164, 165, 166, 167, 168, 170,
    171, 172, 173, 174, 175, 176, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187,
    188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
    204, 205, 205, 206, 207, 208, 209, 210, 211, 211, 212, 213, 214, 215, 215, 216,
    217, 218, 219, 219, 220, 221, 222, 222, 223, 224, 224, 225, 226, 226, 227, 228,
    228, 229, 230, 230, 231, 232, 232, 233, 233, 234, 235, 235, 236, 236, 237, 237,
    238, 238, 239, 239, 240, 240, 241, 241, 242, 242, 243, 243, 244, 244, 244, 245,
    245, 246, 246, 246, 247, 247, 248, 248, 248, 249, 249, 249, 250, 250, 250, 250,
    251, 251, 251, 251, 252, 252, 252, 252, 253, 253, 253, 253, 253, 254, 254, 254,
    254, 254, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 256]


>>>>>>> 3eb85d509c3ae985826701308b81c0e535836380
class whitening403:
    # 美白后的图像
    image = []

<<<<<<< HEAD
    # 通过图层混合实现图像美白
    def whiten403(self, img, alpha):
        height, width, _ = img.shape
        img1 = img.copy()
        # 新建一个图层，将这个图层设置为白色
        for i in range(height):
            for j in range(width):
                img1[i, j][0] = 255
                img1[i, j][1] = 255
                img1[i, j][2] = 255
        gamma = 0
        # 将图像和图层进行颜色混合
        # dst = img*beta + blur*alpha + gamma
        img_add = cv2.addWeighted(img, 1-alpha, img1, alpha, gamma)
        cv2.imwrite('temp/temp.jpg', img_add)
        img = Image.open('temp/temp.jpg')
        # 增强对比度
        contraster = ImageEnhance.Contrast(img)
        contrast = 1.2
        img_contrasted = contraster.enhance(contrast)
        # 增强亮度
        brighter = ImageEnhance.Brightness(img_contrasted)
        bright = 1.1
        img_brighted = brighter.enhance(bright)
        # Image转opencv
        self.image = cv2.cvtColor(numpy.asarray(img_brighted), cv2.COLOR_RGB2BGR)
        # cv2.namedWindow('result', 0)
        # cv2.imshow('result', self.image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
=======
    # 通过颜色查找表实现图像美白
    def whiten403(self, img, alpha):
        height, width, _ = img.shape
        # 创建双边过滤器实例
        img = cv2.bilateralFilter(img, 9, 75, 75)
        # 将像素映射到颜色查找表中
        for i in range(height):
            for j in range(width):
                B = img[i, j][0]
                G = img[i, j][1]
                R = img[i, j][2]
                img[i, j][0] = Color_list[B]
                img[i, j][1] = Color_list[G]
                img[i, j][2] = Color_list[R]
        cv2.imwrite('imgWhiten/res.jpg', img)
        img = Image.open('imgWhiten/res.jpg')
        # 增强对比度
        contraster = ImageEnhance.Contrast(img)
        # contrast = 1.2
        img_contrasted = contraster.enhance(alpha)
        # 增强色度
        colorer = ImageEnhance.Color(img_contrasted)
        # color = 1.2
        img_colored = colorer.enhance(alpha)
        # Image转opencv
        self.image = cv2.cvtColor(numpy.asarray(img_colored), cv2.COLOR_RGB2BGR)
        cv2.namedWindow('result', 0)
        cv2.imshow('result', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
>>>>>>> 3eb85d509c3ae985826701308b81c0e535836380


if __name__ == '__main__':
    whiten = whitening403()
<<<<<<< HEAD
    ima = cv2.imread('testImage/girl4.png')
    cv2.namedWindow('region', 0)
    cv2.imshow('region', ima)
    whiten.whiten403(ima, 0.12)
=======
    ima = cv2.imread('girl4.png')
    cv2.namedWindow('region', 0)
    cv2.imshow('region', ima)
    whiten.whiten403(ima, 0.8)
>>>>>>> 3eb85d509c3ae985826701308b81c0e535836380
