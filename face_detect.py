"""
函数：face_detect
参数：
image：原始灰度图像
功能：人脸以及五官检测
"""
import dlib


def face_detect_424(image):
    # 获得人脸检测器
    detector = dlib.get_frontal_face_detector()
    # 获得人脸关键点预测器
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    # 获得图片中所有人脸检测矩形框的4点坐标
    faces = detector(image, 0)
    # 初始化所有人脸的68个关键点位置列表
    all_shape = []
    # 遍历所有检测到的人脸
    for face in faces:
        # 获得68个关键点的位置
        all_shape.append(predictor(image, face))
    # 返回人脸框位置，五官位置
    return faces, all_shape
