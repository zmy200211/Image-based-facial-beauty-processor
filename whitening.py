# -*- coding: utf-8 -*-
"""
Created on 2023年5月30日
@author 许梦媛
@description: 本程序通过图层混合实现对人脸美白
@version 2.0
@CopyRight: CQUT
"""
from PIL import Image
import cv2
from PIL import ImageEnhance
import numpy

class whitening403:
    # 美白后的图像
    image = []

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


if __name__ == '__main__':
    whiten = whitening403()
    ima = cv2.imread('testImage/girl4.png')
    cv2.namedWindow('region', 0)
    cv2.imshow('region', ima)
    whiten.whiten403(ima, 0.12)
