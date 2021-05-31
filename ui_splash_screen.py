from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide2.QtGui import QFont
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet(
            "QFrame {background-color: rgb(155, 192, 52);color: rgb(220, 220, 220);border-radius: 10px;}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setGeometry(QRect(0, 90, 661, 61))
        font = QFont()
        font.setFamily("Chiller")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(36, 34, 37);font: 48pt \"Chiller\";")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setGeometry(QRect(0, 150, 661, 31))
        font = QFont()
        font.setFamily("Chiller")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(242, 87, 85);font: 26pt \"Chiller\";")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QRect(50, 280, 561, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    background-color: rgb(36, 34, 37);\n"
                                       "    color: rgb(200, 200, 200);\n"
                                       "    border-style: none;\n"
                                       "    border-radius: 10px;\n"
                                       "    text-align: center;\n"
                                       "    font: 16pt \"Chiller\";\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "    border-radius: 10px;\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(36, 34, 37, 255), stop:1 rgab(155, 192, 52, 255));\n"
                                       "}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setGeometry(QRect(0, 320, 661, 21))
        font = QFont()
        font.setFamily("Chiller")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("color: rgb(135, 232, 155);\n"
                                         "font: 24pt \"Chiller\";")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setGeometry(QRect(20, 350, 621, 21))
        font = QFont()
        font.setFamily("Chiller")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("font: 16pt \"Chiller\";\n"
                                         "color: rgb(36, 34, 37);")
        self.label_credits.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_title.setText(_translate("SplashScreen", "<strong>YOUR</strong> APP NAME"))
        self.label_description.setText(_translate("SplashScreen", "<strong>APP</strong> DESCRIPTION"))
        self.label_loading.setText(_translate("SplashScreen", "loading..."))
        self.label_credits.setText(_translate("SplashScreen",
                                              "<html><head/><body><p><span style=\" font-weight:600;\">Created</span>: Zuzanna Bek</p></body></html>"))
