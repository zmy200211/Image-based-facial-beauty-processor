# -*- coding: utf-8 -*-
"""
Created on 2023年5月29日
@author 许梦媛
@description: 本程序用于对人脸磨皮
@version 1.0
@CopyRight: CQUT
"""
import cv2
from PIL import Image
from PIL import ImageEnhance
import numpy

class buffing403:
    # 磨皮后的图像
    image = []

    # 对传入的图片进行磨皮处理
    def buff403(self, img, alpha):
        # 图像滤波
        # 创建双边过滤器实例
        blur = cv2.bilateralFilter(img, 9, 75, 75)

        # 图像融合
        beta = 1 - alpha
        gamma = 0
        # dst = img*beta + blur*alpha + gamma
        img_add = cv2.addWeighted(img, beta, blur, alpha, gamma)
        cv2.imwrite('temp/temp.jpg', img_add)

        # 图像锐化
        img_add = Image.open('temp/temp.jpg')
        # 增强锐度
        sharper = ImageEnhance.Sharpness(img_add)
        sharpness = 1.5
        img_sharped = sharper.enhance(sharpness)
        # 增强对比度
        contraster = ImageEnhance.Contrast(img_sharped)
        contrast = 1.15
        img_contrasted = contraster.enhance(contrast)
        # Image转opencv
        self.image = cv2.cvtColor(numpy.asarray(img_contrasted), cv2.COLOR_RGB2BGR)
        # cv2.namedWindow('result', 0)
        # cv2.imshow('result', self.image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


if __name__ == '__main__':
    buff = buffing403()
    ima = cv2.imread('girl2.jpg')
    cv2.namedWindow('region', 0)
    cv2.imshow('region', ima)
    buff.buff403(ima, 0.1)






































