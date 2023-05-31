# -*- coding: utf-8 -*-
"""
Created on 2023年5月30日
@author 许梦媛
@description: 本程序利用Qtdesigner创建界面
@version 5.0
@CopyRight: CQUT
"""
import cv2
from PIL import ImageQt

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog

import buffing
import whitening
from auto_lift_face import start_auto_face_lift_424


class Ui_MainWindow403(object):
    # 打开的文件路径
    filepath = ''
    # 捕捉摄像头
    camera = cv2.VideoCapture(0)  # 0代表是打开笔记本的内置摄像头
    # 设置定时器
    timer = QTimer()
    # 显示视频时的图像
    photo = []

    def setupUi403(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(53, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(130, 0))
        self.horizontalSlider.setMaximum(30)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setProperty("value", 7)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.horizontalSlider)
        spacerItem2 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setMinimumSize(QtCore.QSize(130, 0))
        self.horizontalSlider_4.setMaximum(30)
        self.horizontalSlider_4.setSingleStep(1)
        self.horizontalSlider_4.setPageStep(1)
        self.horizontalSlider_4.setProperty("value", 20)
        self.horizontalSlider_4.setTracking(True)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setInvertedAppearance(False)
        self.horizontalSlider_4.setInvertedControls(False)
        self.horizontalSlider_4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_4.setTickInterval(1)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.verticalLayout_3.addWidget(self.horizontalSlider_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setProperty("value", 40)
        self.horizontalSlider_2.setMinimumSize(QtCore.QSize(130, 0))
        self.horizontalSlider_2.setMinimum(-50)
        self.horizontalSlider_2.setMaximum(50)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setPageStep(10)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_3.addWidget(self.horizontalSlider_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setMinimumSize(QtCore.QSize(130, 0))
        self.horizontalSlider_3.setMinimum(-50)
        self.horizontalSlider_3.setMaximum(50)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout_3.addWidget(self.horizontalSlider_3)
        spacerItem5 = QtWidgets.QSpacerItem(17, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(500, 500))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem8 = QtWidgets.QSpacerItem(20, 148, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem9 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem10 = QtWidgets.QSpacerItem(20, 98, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        spacerItem11 = QtWidgets.QSpacerItem(20, 88, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        spacerItem12 = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem14 = QtWidgets.QSpacerItem(52, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_5.clicked.connect(self.open403)  # 打开图片
        self.pushButton_6.clicked.connect(self.cameraOpen403)  # 打开摄像头
        self.pushButton_7.clicked.connect(self.takePhoto403)  # 拍照
        self.pushButton.clicked.connect(self.buffe403)  # 磨皮
        self.horizontalSlider.sliderReleased.connect(self.buffe403)  # 拖动滑块改变磨皮程度
        self.pushButton_3.clicked.connect(self.white403)  # 美白
        self.horizontalSlider_4.sliderReleased.connect(self.white403)  # 拖动滑块改变美白程度
        self.pushButton_2.clicked.connect(self.liftFace403)  # 瘦脸
        self.horizontalSlider_2.sliderReleased.connect(self.liftFace403)  # 拖动滑块改变瘦脸程度
        self.pushButton_4.clicked.connect(self.bigEye403)  # 大眼
        self.horizontalSlider_3.sliderReleased.connect(self.bigEye403)  # 拖动滑块改变大眼程度

        self.retranslateUi403(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi403(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "磨皮"))
        self.pushButton_3.setText(_translate("MainWindow", "美白"))
        self.pushButton_2.setText(_translate("MainWindow", "瘦脸"))
        self.pushButton_4.setText(_translate("MainWindow", "大眼"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_5.setText(_translate("MainWindow", "打开图片"))
        self.pushButton_6.setText(_translate("MainWindow", "打开摄像头"))
        self.pushButton_7.setText(_translate("MainWindow", "关闭摄像头"))

    # 打开图像
    def open403(self):
        # 获取打开的文件的路径
        self.filepath = QFileDialog.getOpenFileName()[0]
        # 读取图像
        img = QPixmap(self.filepath)
        # 获取图像的宽和高
        w = img.width()
        h = img.height()
        # 根据图像与label的比例，最大化图像在label中的显示
        ratio = max(w / self.label.width(), h / self.label.height())
        img.setDevicePixelRatio(ratio)
        # 图像在label中居中显示
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setPixmap(img)

    # 打开摄像头
    def cameraOpen403(self):
        # 判断摄像头是否成功打开
        if self.camera.isOpened():
            # 定时器会以恒定的间隔发出timeout信号
            self.timer.timeout.connect(self.show_pic403)
            # 开始定时
            self.timer.start()
            print("beginning！")
        else:
            print('error')

    # 显示视频图像
    def show_pic403(self):
        # 一帧一帧读取图像
        flag, frame = self.camera.read()
        if flag:
            self.photo = frame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 视频流的长和宽
            height, width = frame.shape[:2]
            pixmap = QImage(frame, width, height, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(pixmap)
            # 获取是视频流和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
            ratio = max(width / self.label.width(), height / self.label.height())
            pixmap.setDevicePixelRatio(ratio)
            # 视频流置于label中间部分播放
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setPixmap(pixmap)

    # 拍照
    def takePhoto403(self):
        self.timer.stop()
        print("stopping！")
        cv2.imwrite('photos/temp.jpg', self.photo)
        self.filepath = 'photos/temp.jpg'

    # 磨皮
    def buffe403(self):
        # 磨皮的程度
        alpha = float(self.horizontalSlider.value())/10
        self.show_buff403(alpha)

    # 根据滚动条显示磨皮图像
    def show_buff403(self, alpha):
        # 创建类的实例
        buff = buffing.buffing403()
        # 读取图片
        ima = cv2.imread(self.filepath)
        buff.buff403(ima, alpha)
        # 存储到指定路径下以便以QPixmap读取图像
        cv2.imwrite('temp/temp.jpg', buff.image)
        pixmap = QPixmap('temp/temp.jpg')
        # 获取是图像和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
        ratio = max(pixmap.width() / self.label.width(), pixmap.height() / self.label.height())
        pixmap.setDevicePixelRatio(ratio)
        # 图像置于label中间部分显示
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setPixmap(pixmap)

    # 美白
    def white403(self):
        # 美白的程度
        alpha = float(self.horizontalSlider_4.value()) / 10
        self.show_white403(3.0-alpha)

    # 根据滚动条显示美白程度
    def show_white403(self, alpha):
        # 创建类的实例
        white = whitening.whitening403()
        # 读取图片
        ima = cv2.imread(self.filepath)
        white.whiten403(ima, alpha)
        # 存储到指定路径下以便以QPixmap读取图像
        cv2.imwrite('temp/temp.jpg', white.image)
        pixmap = QPixmap('temp/temp.jpg')
        # 获取是图像和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
        ratio = max(pixmap.width() / self.label.width(), pixmap.height() / self.label.height())
        pixmap.setDevicePixelRatio(ratio)
        # 图像置于label中间部分显示
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setPixmap(pixmap)

    # 瘦脸
    def liftFace403(self):
        # 瘦脸的程度
        alpha = float(self.horizontalSlider_4.value())
        self.show_lift403(alpha)

    # 根据滚动条显示美白程度
    def show_lift403(self, alpha):
        img = cv2.imread(self.filepath)
        result = start_auto_face_lift_424(img, alpha)
        # 存储到指定路径下以便以QPixmap读取图像
        cv2.imwrite('temp/temp.jpg', result)
        pixmap = QPixmap('temp/temp.jpg')
        # 获取是图像和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
        ratio = max(pixmap.width() / self.label.width(), pixmap.height() / self.label.height())
        pixmap.setDevicePixelRatio(ratio)
        # 图像置于label中间部分显示
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setPixmap(pixmap)

    # 大眼
    def bigEye403(self):
        # 大眼的程度
        alpha = float(self.horizontalSlider_4.value())
        self.show_bigEye403(alpha)

    # 根据滚动条显示大眼程度
    def show_bigEye403(self, alpha):
        pass



