# -*- coding: utf-8 -*-
"""
Created on 2023年5月30日
@author 许梦媛
@description: 本程序利用Qtdesigner创建界面
@version 5.0
@CopyRight: CQUT
"""
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
import auto_big_eyes
import auto_face_lift
import buffing
import whitening
import add_blush

class Ui_MainWindow403(QWidget):
    # 打开的文件路径
    filepath = ''
    # 捕捉摄像头
    camera = cv2.VideoCapture(0)  # 0代表是打开笔记本的内置摄像头
    # 设置定时器
    timer = QTimer()
    # 显示视频时的图像
    photo = []
    # 创建磨皮类的实例
    buff = buffing.buffing403()
    # 创建美白类的实例
    white = whitening.whitening403()

    def setupUi403(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1976, 1192)
        mainWindow.move(0, 0)
        mainWindow.showMaximized()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(17, 81, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
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
        self.verticalLayout_5.addWidget(self.horizontalSlider)
        spacerItem2 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setMinimumSize(QtCore.QSize(130, 0))
        self.horizontalSlider_4.setMaximum(30)
        self.horizontalSlider_4.setSingleStep(1)
        self.horizontalSlider_4.setPageStep(1)
        self.horizontalSlider_4.setProperty("value", 15)
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
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton_10.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_3.addWidget(self.pushButton_10)
        self.horizontalSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_5.setMinimumSize(QtCore.QSize(130, 0))
        self.horizontalSlider_5.setMinimum(0)
        self.horizontalSlider_5.setMaximum(10)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.verticalLayout_3.addWidget(self.horizontalSlider_5)
        spacerItem6 = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setStyleSheet("font: 75 14pt \"Bahnschrift\";\n"
                                        "font: 87 14pt \"Arial Black\";\n"
                                        "color: rgb(199, 84, 80);\n"
                                        "")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setStyleSheet("color: rgb(73, 156, 84);\n"
                                        "font: 75 14pt \"Arial Narrow\";\n"
                                        "font: 87 14pt \"Arial Black\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(126, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        spacerItem8 = QtWidgets.QSpacerItem(26, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(750, 750))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem10 = QtWidgets.QSpacerItem(20, 148, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem11 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem12 = QtWidgets.QSpacerItem(20, 98, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        spacerItem13 = QtWidgets.QSpacerItem(20, 88, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        spacerItem14 = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem14)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem15)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem16 = QtWidgets.QSpacerItem(52, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.pushButton_5.clicked.connect(self.open403)  # 打开图片
        self.pushButton_6.clicked.connect(self.cameraOpen403)  # 打开摄像头
        self.pushButton_7.clicked.connect(self.takePhoto403)  # 拍照
        self.pushButton.clicked.connect(self.buffe403)  # 磨皮
        self.horizontalSlider.sliderPressed.connect(self.closeButton403)
        self.horizontalSlider.sliderPressed.connect(self.closeSlider403)
        self.horizontalSlider.sliderReleased.connect(self.buffe403)  # 拖动滑块改变磨皮程度
        self.horizontalSlider.sliderReleased.connect(self.openButton403)
        self.pushButton_3.clicked.connect(self.white403)  # 美白
        self.horizontalSlider_4.sliderPressed.connect(self.closeButton403)
        self.horizontalSlider_4.sliderPressed.connect(self.closeSlider_4403)
        self.horizontalSlider_4.sliderReleased.connect(self.white403)  # 拖动滑块改变美白程度
        self.horizontalSlider_4.sliderReleased.connect(self.openButton403)
        self.pushButton_2.clicked.connect(self.liftFace403)  # 瘦脸
        self.horizontalSlider_2.sliderPressed.connect(self.closeButton403)
        self.horizontalSlider_2.sliderPressed.connect(self.closeSlider_2403)
        self.horizontalSlider_2.sliderReleased.connect(self.liftFace403)  # 拖动滑块改变瘦脸程度
        self.horizontalSlider_2.sliderReleased.connect(self.openButton403)
        self.pushButton_4.clicked.connect(self.bigEye403)  # 大眼
        self.horizontalSlider_3.sliderPressed.connect(self.closeButton403)
        self.horizontalSlider_3.sliderPressed.connect(self.closeSlider_3403)
        self.horizontalSlider_3.sliderReleased.connect(self.bigEye403)  # 拖动滑块改变大眼程度
        self.horizontalSlider_3.sliderReleased.connect(self.openButton403)
        self.pushButton_10.clicked.connect(self.addBlush403)  # 腮红
        self.horizontalSlider_5.sliderPressed.connect(self.closeButton403)
        self.horizontalSlider_5.sliderPressed.connect(self.closeSlider_5403)
        self.horizontalSlider_5.sliderReleased.connect(self.addBlush403)  # 拖动滑块改变腮红程度
        self.horizontalSlider_5.sliderReleased.connect(self.openButton403)
        self.pushButton_8.clicked.connect(self.confirm403)  # 确定调节效果
        self.pushButton_9.clicked.connect(self.cancle403)  # 撤销调节效果

        self.retranslateUi403(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi403(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "美图秀儿"))
        self.pushButton.setText(_translate("mainWindow", "磨皮"))
        self.pushButton_3.setText(_translate("mainWindow", "美白"))
        self.pushButton_2.setText(_translate("mainWindow", "瘦脸"))
        self.pushButton_4.setText(_translate("mainWindow", "大眼"))
        self.pushButton_10.setText(_translate("mainWindow", "腮红"))
        self.pushButton_9.setText(_translate("mainWindow", "×"))
        self.pushButton_8.setText(_translate("mainWindow", "√"))
        self.label.setText(_translate("mainWindow", "TextLabel"))
        self.pushButton_5.setText(_translate("mainWindow", "打开图片"))
        self.pushButton_6.setText(_translate("mainWindow", "打开摄像头"))
        self.pushButton_7.setText(_translate("mainWindow", "拍照"))

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
        alpha = float(self.horizontalSlider.value()) / 10
        self.show_buff403(alpha)

    # 根据滚动条显示磨皮图像
    def show_buff403(self, alpha):
        # 读取图片
        ima = cv2.imread(self.filepath)
        self.buff.buff403(ima, alpha)
        # 存储到指定路径下以便以QPixmap读取图像
        cv2.imwrite('temp/temp.jpg', self.buff.image)
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
        alpha = float(self.horizontalSlider_4.value()) / 100
        self.show_white403(alpha)

    # 根据滚动条显示美白程度
    def show_white403(self, alpha):
        # 读取图片
        ima = cv2.imread(self.filepath)
        self.white.whiten403(ima, alpha)
        # 存储到指定路径下以便以QPixmap读取图像
        cv2.imwrite('temp/temp.jpg', self.white.image)
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
        alpha = float(self.horizontalSlider_2.value())
        print(alpha)
        self.show_lift403(alpha)

    # 根据滚动条显示瘦脸程度
    def show_lift403(self, alpha):
        img = cv2.imread(self.filepath)
        result = auto_face_lift.start_auto_face_lift_424(img, alpha)
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
        alpha = float(self.horizontalSlider_3.value())
        self.show_bigEye403(alpha)

    # 根据滚动条显示大眼程度
    def show_bigEye403(self, alpha):
        img = cv2.imread(self.filepath)
        result = auto_big_eyes.start_auto_big_eyes_424(img, alpha)
        # 存储到指定路径下以便以QPixmap读取图像
        cv2.imwrite('temp/temp.jpg', result)
        pixmap = QPixmap('temp/temp.jpg')
        # 获取是图像和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
        ratio = max(pixmap.width() / self.label.width(), pixmap.height() / self.label.height())
        pixmap.setDevicePixelRatio(ratio)
        # 图像置于label中间部分显示
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setPixmap(pixmap)

    # 添加腮红
    def addBlush403(self):
        # 腮红的程度
        alpha = float(self.horizontalSlider_5.value())/10
        print(alpha)
        self.show_addBlush403(alpha)

    # 根据滚动条显示大眼程度
    def show_addBlush403(self, alpha):
        img = cv2.imread(self.filepath)
        result = add_blush.start_add_blush_424(img, alpha)
        # 存储到指定路径下以便以QPixmap读取图像
        cv2.imwrite('temp/temp.jpg', result)
        pixmap = QPixmap('temp/temp.jpg')
        # 获取是图像和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
        ratio = max(pixmap.width() / self.label.width(), pixmap.height() / self.label.height())
        pixmap.setDevicePixelRatio(ratio)
        # 图像置于label中间部分显示
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setPixmap(pixmap)

    # 确定修正效果
    def confirm403(self):
        img = cv2.imread('temp/temp.jpg')
        cv2.imwrite('confirmImage/confirm.jpg', img)
        # 之后修改是在这个基础上
        self.filepath = 'confirmImage/confirm.jpg'

    # 撤销修正效果，即显示修改之前的原图
    def cancle403(self):
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

    # 关闭所有按钮
    def closeButton403(self):
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_10.setEnabled(False)

    # 关闭对应的滑动条
    def closeSlider403(self):
        self.horizontalSlider_2.setEnabled(False)
        self.horizontalSlider_3.setEnabled(False)
        self.horizontalSlider_4.setEnabled(False)
        self.horizontalSlider_5.setEnabled(False)

    # 关闭对应的滑动条
    def closeSlider_2403(self):
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider_3.setEnabled(False)
        self.horizontalSlider_4.setEnabled(False)
        self.horizontalSlider_5.setEnabled(False)

    # 关闭对应的滑动条
    def closeSlider_3403(self):
        self.horizontalSlider_2.setEnabled(False)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider_4.setEnabled(False)
        self.horizontalSlider_5.setEnabled(False)

    # 关闭对应的滑动条
    def closeSlider_4403(self):
        self.horizontalSlider_2.setEnabled(False)
        self.horizontalSlider_3.setEnabled(False)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider_5.setEnabled(False)

    # 关闭对应的滑动条
    def closeSlider_5403(self):
        self.horizontalSlider_2.setEnabled(False)
        self.horizontalSlider_3.setEnabled(False)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider_4.setEnabled(False)

    # 打开所有按钮
    def openButton403(self):
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider_2.setEnabled(True)
        self.horizontalSlider_3.setEnabled(True)
        self.horizontalSlider_4.setEnabled(True)
        self.horizontalSlider_5.setEnabled(True)


