from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1038, 718)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(36, 34, 37);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 70))
        self.main_header.setStyleSheet(u"background-color: rgb(155, 192, 52);")
        self.main_header.setFrameShape(QFrame.NoFrame)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title_bar_container = QFrame(self.main_header)
        self.title_bar_container.setObjectName(u"title_bar_container")
        self.title_bar_container.setStyleSheet(u"background-color: rgb(155, 192, 52);")
        self.title_bar_container.setFrameShape(QFrame.StyledPanel)
        self.title_bar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.title_bar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle = QFrame(self.title_bar_container)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setMinimumSize(QSize(75, 0))
        self.left_menu_toggle.setMaximumSize(QSize(85, 16777215))
        self.left_menu_toggle.setStyleSheet(u"background-color: rgb(155, 192, 52);")
        self.left_menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.left_menu_toggle)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setMinimumSize(QSize(85, 0))
        self.menu_btn.setMaximumSize(QSize(16777215, 16777215))
        self.menu_btn.setStyleSheet(u"QPushButton {\n"
                                    "	border-style: outset;\n"
                                    "	border-radius: 25px;\n"
                                    "	border-color: rgb(36, 34, 37);\n"
                                    "	padding: 4px;\n"
                                    "}\n"
                                    "QPushButton::pressed {\n"
                                    "	border-style: outset;\n"
                                    "	border-radius: 25px;\n"
                                    "	border-color: rgb(36, 34, 37);\n"
                                    "	padding: 4px;\n"
                                    "	background-color: rgb(36, 34, 37);\n"
                                    "}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.menu_btn)

        self.horizontalLayout_5.addWidget(self.left_menu_toggle)

        self.title_bar = QFrame(self.title_bar_container)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777015, 70))
        self.title_bar.setStyleSheet(u"background-color: rgb(155, 192, 52);")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.title_bar)

        self.horizontalLayout_3.addWidget(self.title_bar_container)

        self.top_right_btns = QFrame(self.main_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        self.top_right_btns.setMaximumSize(QSize(75, 16777215))
        self.top_right_btns.setStyleSheet(u"background-color: rgb(155, 192, 52);")
        self.top_right_btns.setFrameShape(QFrame.HLine)
        self.top_right_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.top_right_btns)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon1)
        self.minimize_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.minimize_btn)

        self.close_btn = QPushButton(self.top_right_btns)
        self.close_btn.setObjectName(u"close_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/error.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon2)
        self.close_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.close_btn, 0, Qt.AlignRight | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.top_right_btns)

        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: rgb(36, 34, 37);")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMinimumSize(QSize(85, 0))
        self.left_side_menu.setMaximumSize(QSize(85, 16777215))
        self.left_side_menu.setStyleSheet(u"background-color: rgb(155, 192, 52);")
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.profile_btn = QPushButton(self.left_side_menu)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setMinimumSize(QSize(0, 75))
        font = QFont()
        font.setFamily(u"Chiller")
        font.setPointSize(28)
        self.profile_btn.setFont(font)
        self.profile_btn.setStyleSheet(u"QPushButton {\n"
                                       "	background-image: url(:/icons/icons/buka.png);\n"
                                       "	background-repeat: none;\n"
                                       "	background-position: center left;\n"
                                       "	border-style: outset;\n"
                                       "	border-radius: 37px;\n"
                                       "	border-color: rgb(36, 34, 37);\n"
                                       "	padding-left: 100px;\n"
                                       "}\n"
                                       "QPushButton::pressed {\n"
                                       "	background-image: url(:/icons/icons/buka.png);\n"
                                       "	background-repeat: none;\n"
                                       "	background-position: center left;\n"
                                       "	border-style: outset;\n"
                                       "	border-radius: 37px;\n"
                                       "	border-color: rgb(36, 34, 37);\n"
                                       "	padding-left: 100px;\n"
                                       "	background-color: rgb(36, 34, 37);\n"
                                       "}")
        self.profile_btn.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.profile_btn)

        self.time_btn = QPushButton(self.left_side_menu)
        self.time_btn.setObjectName(u"time_btn")
        self.time_btn.setMinimumSize(QSize(0, 75))
        self.time_btn.setFont(font)
        self.time_btn.setStyleSheet(u"QPushButton {\n"
                                    "	background-image: url(:/icons/icons/time.png);\n"
                                    "	background-repeat: none;\n"
                                    "	background-position: center left;\n"
                                    "	border-style: outset;\n"
                                    "	border-radius: 37px;\n"
                                    "	border-color: rgb(36, 34, 37);\n"
                                    "	padding-left: 100px;\n"
                                    "}\n"
                                    "QPushButton::pressed {\n"
                                    "	background-image: url(:/icons/icons/time.png);\n"
                                    "	background-repeat: none;\n"
                                    "	background-position: center left;\n"
                                    "	border-style: outset;\n"
                                    "	border-radius: 37px;\n"
                                    "	border-color: rgb(36, 34, 37);\n"
                                    "	padding-left: 100px;\n"
                                    "	background-color: rgb(36, 34, 37);\n"
                                    "}")
        self.time_btn.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.time_btn)

        self.notes_btn = QPushButton(self.left_side_menu)
        self.notes_btn.setObjectName(u"notes_btn")
        self.notes_btn.setMinimumSize(QSize(0, 75))
        self.notes_btn.setFont(font)
        self.notes_btn.setStyleSheet(u"QPushButton {\n"
                                     "	background-image: url(:/icons/icons/notes.png);\n"
                                     "	background-repeat: none;\n"
                                     "	background-position: center left;\n"
                                     "	border-style: outset;\n"
                                     "	border-radius: 37px;\n"
                                     "	border-color: rgb(36, 34, 37);\n"
                                     "	padding-left: 100px;\n"
                                     "}\n"
                                     "QPushButton::pressed {\n"
                                     "	background-image: url(:/icons/icons/notes.png);\n"
                                     "	background-repeat: none;\n"
                                     "	background-position: center left;\n"
                                     "	border-style: outset;\n"
                                     "	border-radius: 37px;\n"
                                     "	border-color: rgb(36, 34, 37);\n"
                                     "	padding-left: 100px;\n"
                                     "	background-color: rgb(36, 34, 37);\n"
                                     "}")
        self.notes_btn.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.notes_btn)

        self.settings_btn = QPushButton(self.left_side_menu)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(0, 75))
        self.settings_btn.setFont(font)
        self.settings_btn.setStyleSheet(u"QPushButton {\n"
                                        "	background-image: url(:/icons/icons/settings.png);\n"
                                        "	background-repeat: none;\n"
                                        "	background-position: center left;\n"
                                        "	border-style: outset;\n"
                                        "	border-radius: 37px;\n"
                                        "	border-color: rgb(36, 34, 37);\n"
                                        "	padding-left: 100px;\n"
                                        "}\n"
                                        "QPushButton::pressed {\n"
                                        "	background-image: url(:/icons/icons/settings.png);\n"
                                        "	background-repeat: none;\n"
                                        "	background-position: center left;\n"
                                        "	border-style: outset;\n"
                                        "	border-radius: 37px;\n"
                                        "	border-color: rgb(36, 34, 37);\n"
                                        "	padding-left: 100px;\n"
                                        "	background-color: rgb(36, 34, 37);\n"
                                        "}")
        self.settings_btn.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.settings_btn)

        self.horizontalLayout.addWidget(self.left_side_menu)

        self.right_side_menu = QFrame(self.main_body)
        self.right_side_menu.setObjectName(u"right_side_menu")
        self.right_side_menu.setStyleSheet(u"background-color: rgb(36, 34, 37);")
        self.right_side_menu.setFrameShape(QFrame.NoFrame)
        self.right_side_menu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.right_side_menu)

        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMaximumSize(QSize(16777215, 35))
        self.main_footer.setStyleSheet(u"background-color: rgb(36, 34, 37);")
        self.main_footer.setFrameShape(QFrame.StyledPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn.setText("")
        self.minimize_btn.setText("")
        self.close_btn.setText("")
        self.profile_btn.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.time_btn.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.notes_btn.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
