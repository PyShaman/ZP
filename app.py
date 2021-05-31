import sys
from pathlib import Path
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QPropertyAnimation
from PySide2.QtGui import QColor, QPixmap
from PySide2.QtUiTools import loadUiType
from PySide2.QtWidgets import *

from ui_splash_screen import Ui_SplashScreen

COUNTER = 0
# FORM_CLASS, _ = loadUiType(resource_path("zuzia_test.ui"))
FORM_CLASS, _ = loadUiType(str(Path("zuzia_main_window.ui")))


class Main(QMainWindow, FORM_CLASS):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setupUi(self)
        self.ui_buttons()
        self.drag_pos = QtCore.QPoint()
        self.title_bar.mouseMoveEvent = self.mouse_move_event

    # def mouse_press_event(self, event):
    #     self.drag_pos = event.globalPos()

    def mouse_move_event(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.drag_pos)
            self.drag_pos = event.globalPos()
            event.accept()

        print(self.drag_pos)

        # self.main_header.mouseMoveEvent = self.move_window()

    # def move_window(self):
    #     if not QMainWindow.isMaximized(self):
    #         if self.buttons() == QtCore.Qt.LeftButton:
    #
    #             self.clickPosition = self.globalPos()
    #             self.move(self.pos() + self.globalPos() - self.clickPosition)
    #
    #             self.accept()

    def ui_buttons(self):
        self.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.close_btn.clicked.connect(lambda: self.close())
        self.menu_btn.clicked.connect(lambda: self.slide_left_side_menu())
        # self.pushButton_4.clicked.connect(self.do_smth)
        # self.pushButton_3.clicked.connect(self.display_image)

    def slide_left_side_menu(self):
        width = self.left_side_menu.width()
        if width == 85:
            new_width = 250
        else:
            new_width = 85

        self.animation = QPropertyAnimation(self.left_side_menu, b'minimumWidth')
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mouse_press_event(self, event):
        self.clickPosition = event.globalPos()

    # def do_smth(self):
    #     self.pushButton_4.setStyleSheet("""
    #     QPushButton
    #     {
    #     font: 16pt "Segoe UI";
    #     background-color : rgb(220, 0, 0);
    #     color: rgb(220, 220, 220);
    #     border-radius: 10px;
    #     }
    #     """
    #                                     )
    #
    # def display_image(self):
    #     pix = QPixmap("pika2.png").scaled(450, 450)
    #     item = QGraphicsPixmapItem(pix)
    #     scene = QtWidgets.QGraphicsScene(self)
    #     scene.addItem(item)
    #     self.graphicsView.setScene(scene)


class SplashScreen(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        self.show()

    def progress(self):
        global COUNTER
        self.ui.progressBar.setValue(COUNTER)
        if COUNTER > 100:
            self.timer.stop()
            self.main = Main()
            self.main.show()
            self.close()
        COUNTER += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
