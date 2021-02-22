import sys
import os

from PyQt5.uic import loadUiType
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


FORM_CLASS, _ = loadUiType(resource_path("basic_view.ui"))


class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.buttons()

    def buttons(self):
        self.profile.setEnabled(True)
        self.profile.clicked.connect(self.display_image)

    def display_image(self):
        picachu = QLabel(self)
        picachu.setAlignment(Qt.AlignCenter)
        picachu.setToolTip('Hint')
        picachu.setPixmap(QPixmap("pika_no.png"))



def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()



