from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
                                           "	\n"
                                           "	background-color: rgb(155, 192, 52);\n"
                                           "	color: rgb(220, 220, 220);\n"
                                           "	border-radius: 10px;\n"
                                           "}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 90, 661, 61))
        font = QFont()
        font.setFamily(u"Chiller")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(36, 34, 37);\n"
                                       "font: 48pt \"Chiller\";")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 150, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Chiller")
        font1.setPointSize(26)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(242, 87, 85);\n"
                                             "font: 26pt \"Chiller\";")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 280, 561, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
                                       "	background-color: rgb(36, 34, 37);\n"
                                       "	color: rgb(200, 200, 200);\n"
                                       "	border-style: none;\n"
                                       "	border-radius: 10px;\n"
                                       "	text-align: center;\n"
                                       "	font: 16pt \"Chiller\";\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "	border-radius: 10px;\n"
                                       "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(36, 34, 37, 255), stop:1 rgab(155, 192, 52, 255));\n"
                                       "}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 320, 661, 21))
        font2 = QFont()
        font2.setFamily(u"Chiller")
        font2.setPointSize(24)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(135, 232, 155);\n"
                                         "font: 24pt \"Chiller\";")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(20, 350, 621, 21))
        font3 = QFont()
        font3.setFamily(u"Chiller")
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"font: 16pt \"Chiller\";\n"
                                         "color: rgb(36, 34, 37);")
        self.label_credits.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<strong>YOUR</strong> APP NAME", None))
        self.label_description.setText(
            QCoreApplication.translate("SplashScreen", u"<strong>APP</strong> DESCRIPTION", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen",
                                                              u"<html><head/><body><p><span style=\" font-weight:600;\">Created</span>: Zuzanna Bek</p></body></html>",
                                                              None))
