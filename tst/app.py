import sys

from PySide2 import QtCore

from ui_main_window import *
from ui_splash_screen import *

COUNTER = 0


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        self.show()

    def progress(self):
        global COUNTER
        self.ui.progressBar.setValue(COUNTER)
        if COUNTER < 33:
            QtCore.QTimer.singleShot(1250, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        elif 34 > COUNTER < 66:
            QtCore.QTimer.singleShot(2000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        elif COUNTER > 100:
            self.timer.stop()
            QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> COMPLETED"))
            self.main = Main()
            self.main.show()
            self.close()
        COUNTER += 1


class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui_buttons()
        self.click_position = QtCore.QPoint()
        self.ui.title_bar.mouseMoveEvent = self.move_window

    def ui_buttons(self):
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.close_btn.clicked.connect(lambda: self.close())
        self.ui.menu_btn.clicked.connect(lambda: self.slide_left_side_menu())
        # self.pushButton_4.clicked.connect(self.do_smth)
        # self.pushButton_3.clicked.connect(self.display_image)

    def slide_left_side_menu(self):
        width = self.ui.left_side_menu.width()
        if width == 85:
            new_width = 250
        else:
            new_width = 85

        self.animation = QPropertyAnimation(self.ui.left_side_menu, b'minimumWidth')
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mouse_press_event(self, event):
        self.click_position = event.globalPos()

    def move_window(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.click_position)
            self.click_position = event.globalPos()
            event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
