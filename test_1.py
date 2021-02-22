from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QSize


class IrregularWindow(QtWidgets.QWidget):
    def __init__(self):
        super(IrregularWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def sizeHint(self):
        return QSize(1037, 1037) # Set this to the exact image resolution

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        pixmap = QtGui.QPixmap()
        pixmap.load('pika2.png')
        qp.drawPixmap(QPoint(0, 0), pixmap)
        qp.end()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


a = QtWidgets.QApplication([])
rw = IrregularWindow()
rw.show()
a.exec_()