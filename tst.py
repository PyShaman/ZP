from pathlib import Path
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QPropertyAnimation
from PySide2.QtGui import QColor, QPixmap
from PySide2.QtUiTools import loadUiType
from PySide2.QtWidgets import *

from ui_splash_screen import Ui_SplashScreen

FORM_CLASS, _ = loadUiType(str(Path("zuzia_main_window.ui")))
COUNTER = 0


class Main(object):
    def setupUi(self, MainWindow):
        # Connect frame to mouseMoveEvent
        self.title_bar.mouseMoveEvent = self.mouse_move_event
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(QMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QMainWindow)

    def retranslateUi(self, QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QMainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


#    def mouseMoveEvent(self, event):
#        if event.buttons() == QtCore.Qt.LeftButton:
#            self.move(self.pos() + event.globalPos() - self.dragPos)
#            self.dragPos = event.globalPos()
#            event.accept()


class MyWin(QMainWindow, Main):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.dragPos = QtCore.QPoint()

    def mousePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def ui_buttons(self):
        self.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.close_btn.clicked.connect(lambda: self.close())
        self.menu_btn.clicked.connect(lambda: self.slide_left_side_menu())

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
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())