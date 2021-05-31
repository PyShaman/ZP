import sys
from PySide2 import QtCore
from ui_main_window import *


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
        self.show()


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

    def move_window(event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.click_position)
            self.click_position = event.globalPos()
            event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
