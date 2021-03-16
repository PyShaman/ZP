import sys
import os

from PyQt5.uic import loadUiType
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


FORM_CLASS, _ = loadUiType(resource_path("zuzia_test.ui"))


class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.buttons()

    def buttons(self):
        self.pushButton_4.clicked.connect(self.do_smth)
        self.pushButton_3.clicked.connect(self.display_image)

    def do_smth(self):
        self.pushButton_4.setStyleSheet("""
        QPushButton
        {
        font: 16pt "Segoe UI";
        background-color : rgb(220, 0, 0);
        color: rgb(220, 220, 220);
        border-radius: 10px;
        }
        """
                                        )

    def display_image(self):
        pix = QPixmap("pika2.png")
        item = QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene(self)
        scene.addItem(item)
        self.graphicsView.setScene(scene)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
