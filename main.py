from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import interface


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序对象
    MainWindow = QMainWindow()  # 创建主窗口
    ui = interface.Ui_MainWindow403()
    ui.setupUi403(MainWindow)
    MainWindow.show()  # 显示主窗口
    sys.exit(app.exec_())  # 在主线程中退出


