# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# __version__ = "v3.0.1 | 26.01.2026"

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import config_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QSize(600, 500))
        MainWindow.setMaximumSize(QSize(900, 750))
        icon = QIcon()
        icon.addFile(u":/icon/files/config/app/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: whitesmoke;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-size: 18pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_site_rq = QLineEdit(self.centralwidget)
        self.le_site_rq.setObjectName(u"le_site_rq")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_site_rq.sizePolicy().hasHeightForWidth())
        self.le_site_rq.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.le_site_rq)

        self.horizontalSpacer = QSpacerItem(30, 1, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_site = QPushButton(self.centralwidget)
        self.add_site.setObjectName(u"add_site")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_site.sizePolicy().hasHeightForWidth())
        self.add_site.setSizePolicy(sizePolicy1)
        self.add_site.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.add_site)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_delete_site_3 = QPushButton(self.centralwidget)
        self.btn_delete_site_3.setObjectName(u"btn_delete_site_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_delete_site_3.sizePolicy().hasHeightForWidth())
        self.btn_delete_site_3.setSizePolicy(sizePolicy2)
        self.btn_delete_site_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_site_3.setStyleSheet(u"font-size: 16pt;\n"
"border: none")

        self.gridLayout.addWidget(self.btn_delete_site_3, 4, 1, 1, 1)

        self.btn_delete_site_4 = QPushButton(self.centralwidget)
        self.btn_delete_site_4.setObjectName(u"btn_delete_site_4")
        sizePolicy2.setHeightForWidth(self.btn_delete_site_4.sizePolicy().hasHeightForWidth())
        self.btn_delete_site_4.setSizePolicy(sizePolicy2)
        self.btn_delete_site_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_site_4.setStyleSheet(u"font-size: 16pt;\n"
"border: none")

        self.gridLayout.addWidget(self.btn_delete_site_4, 5, 1, 1, 1)

        self.lbl_site_list_2 = QLabel(self.centralwidget)
        self.lbl_site_list_2.setObjectName(u"lbl_site_list_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_site_list_2.sizePolicy().hasHeightForWidth())
        self.lbl_site_list_2.setSizePolicy(sizePolicy3)
        self.lbl_site_list_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lbl_site_list_2.setStyleSheet(u"font-size: 16pt;\n"
"border: none")
        self.lbl_site_list_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_site_list_2, 3, 0, 1, 1)

        self.lbl_site_list_4 = QLabel(self.centralwidget)
        self.lbl_site_list_4.setObjectName(u"lbl_site_list_4")
        sizePolicy3.setHeightForWidth(self.lbl_site_list_4.sizePolicy().hasHeightForWidth())
        self.lbl_site_list_4.setSizePolicy(sizePolicy3)
        self.lbl_site_list_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lbl_site_list_4.setStyleSheet(u"font-size: 16pt;\n"
"border: none")
        self.lbl_site_list_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_site_list_4, 5, 0, 1, 1)

        self.lbl_site_list_1 = QLabel(self.centralwidget)
        self.lbl_site_list_1.setObjectName(u"lbl_site_list_1")
        sizePolicy3.setHeightForWidth(self.lbl_site_list_1.sizePolicy().hasHeightForWidth())
        self.lbl_site_list_1.setSizePolicy(sizePolicy3)
        self.lbl_site_list_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lbl_site_list_1.setStyleSheet(u"font-size: 16pt;\n"
"border: none")
        self.lbl_site_list_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_site_list_1, 2, 0, 1, 1)

        self.btn_next_page = QPushButton(self.centralwidget)
        self.btn_next_page.setObjectName(u"btn_next_page")
        self.btn_next_page.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_next_page.setStyleSheet(u"font-size: 14pt\n"
"")
        self.btn_next_page.setCheckable(False)

        self.gridLayout.addWidget(self.btn_next_page, 7, 1, 1, 1)

        self.btn_delete_site_1 = QPushButton(self.centralwidget)
        self.btn_delete_site_1.setObjectName(u"btn_delete_site_1")
        sizePolicy2.setHeightForWidth(self.btn_delete_site_1.sizePolicy().hasHeightForWidth())
        self.btn_delete_site_1.setSizePolicy(sizePolicy2)
        self.btn_delete_site_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_site_1.setStyleSheet(u"font-size: 16pt;\n"
"border: none")

        self.gridLayout.addWidget(self.btn_delete_site_1, 2, 1, 1, 1)

        self.lbl_site_list_3 = QLabel(self.centralwidget)
        self.lbl_site_list_3.setObjectName(u"lbl_site_list_3")
        sizePolicy3.setHeightForWidth(self.lbl_site_list_3.sizePolicy().hasHeightForWidth())
        self.lbl_site_list_3.setSizePolicy(sizePolicy3)
        self.lbl_site_list_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lbl_site_list_3.setStyleSheet(u"font-size: 16pt;\n"
"border: none")
        self.lbl_site_list_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_site_list_3, 4, 0, 1, 1)

        self.btn_delete_site_2 = QPushButton(self.centralwidget)
        self.btn_delete_site_2.setObjectName(u"btn_delete_site_2")
        sizePolicy2.setHeightForWidth(self.btn_delete_site_2.sizePolicy().hasHeightForWidth())
        self.btn_delete_site_2.setSizePolicy(sizePolicy2)
        self.btn_delete_site_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_site_2.setStyleSheet(u"font-size: 16pt;\n"
"border: none")

        self.gridLayout.addWidget(self.btn_delete_site_2, 3, 1, 1, 1)

        self.btn_delete_site_5 = QPushButton(self.centralwidget)
        self.btn_delete_site_5.setObjectName(u"btn_delete_site_5")
        sizePolicy2.setHeightForWidth(self.btn_delete_site_5.sizePolicy().hasHeightForWidth())
        self.btn_delete_site_5.setSizePolicy(sizePolicy2)
        self.btn_delete_site_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_site_5.setStyleSheet(u"font-size: 16pt;\n"
"border: none")

        self.gridLayout.addWidget(self.btn_delete_site_5, 6, 1, 1, 1)

        self.lbl_site_list_5 = QLabel(self.centralwidget)
        self.lbl_site_list_5.setObjectName(u"lbl_site_list_5")
        sizePolicy3.setHeightForWidth(self.lbl_site_list_5.sizePolicy().hasHeightForWidth())
        self.lbl_site_list_5.setSizePolicy(sizePolicy3)
        self.lbl_site_list_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lbl_site_list_5.setStyleSheet(u"font-size: 16pt;\n"
"border: none")
        self.lbl_site_list_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_site_list_5, 6, 0, 1, 1)

        self.btn_become_page = QPushButton(self.centralwidget)
        self.btn_become_page.setObjectName(u"btn_become_page")
        self.btn_become_page.setStyleSheet(u"font-size: 14pt;")

        self.gridLayout.addWidget(self.btn_become_page, 7, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_list_site = QPushButton(self.centralwidget)
        self.btn_list_site.setObjectName(u"btn_list_site")
        sizePolicy2.setHeightForWidth(self.btn_list_site.sizePolicy().hasHeightForWidth())
        self.btn_list_site.setSizePolicy(sizePolicy2)
        self.btn_list_site.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btn_list_site)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_adctivate = QPushButton(self.centralwidget)
        self.btn_adctivate.setObjectName(u"btn_adctivate")
        sizePolicy2.setHeightForWidth(self.btn_adctivate.sizePolicy().hasHeightForWidth())
        self.btn_adctivate.setSizePolicy(sizePolicy2)
        self.btn_adctivate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_adctivate)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Switch Site", None))
        self.le_site_rq.setText("")
        self.add_site.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0430\u0439\u0442", None))
#if QT_CONFIG(shortcut)
        self.add_site.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_site_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0430\u0439\u0442", None))
        self.btn_delete_site_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0430\u0439\u0442", None))
        self.lbl_site_list_2.setText(QCoreApplication.translate("MainWindow", u"www.site.com", None))
        self.lbl_site_list_4.setText(QCoreApplication.translate("MainWindow", u"www.site.com", None))
        self.lbl_site_list_1.setText(QCoreApplication.translate("MainWindow", u"www.site.com", None))
        self.btn_next_page.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(shortcut)
        self.btn_next_page.setShortcut(QCoreApplication.translate("MainWindow", u"PgUp", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_site_1.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0430\u0439\u0442", None))
        self.lbl_site_list_3.setText(QCoreApplication.translate("MainWindow", u"www.site.com", None))
        self.btn_delete_site_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0430\u0439\u0442", None))
        self.btn_delete_site_5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0430\u0439\u0442", None))
        self.lbl_site_list_5.setText(QCoreApplication.translate("MainWindow", u"www.site.com", None))
        self.btn_become_page.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(shortcut)
        self.btn_become_page.setShortcut(QCoreApplication.translate("MainWindow", u"PgDown", None))
#endif // QT_CONFIG(shortcut)
        self.btn_list_site.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0441\u0430\u0439\u0442\u043e\u0432", None))
        self.btn_adctivate.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443", None))
    # retranslateUi

