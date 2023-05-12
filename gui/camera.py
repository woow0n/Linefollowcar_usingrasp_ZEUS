# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(522, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 20, 441, 521))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.forward = QPushButton(self.gridLayoutWidget)
        self.forward.setObjectName(u"forward")

        self.horizontalLayout.addWidget(self.forward)

        self.backward = QPushButton(self.gridLayoutWidget)
        self.backward.setObjectName(u"backward")

        self.horizontalLayout.addWidget(self.backward)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.screen = QLabel(self.gridLayoutWidget)
        self.screen.setObjectName(u"screen")

        self.gridLayout.addWidget(self.screen, 0, 0, 1, 1)

        self.info = QLabel(self.gridLayoutWidget)
        self.info.setObjectName(u"info")

        self.gridLayout.addWidget(self.info, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 522, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.forward.clicked.connect(MainWindow.forwarding)
        self.backward.clicked.connect(MainWindow.stopping)
        self.pushButton.clicked.connect(MainWindow.turnleft)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.forward.setText(QCoreApplication.translate("MainWindow", u"forward", None))
        self.backward.setText(QCoreApplication.translate("MainWindow", u"backward", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"turnleft", None))
        self.screen.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

