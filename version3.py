
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'version2.ui'
#
# Created: Sun Jul 15 08:01:47 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import init
import sys
u''' main interface class  '''
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 451)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.write_button = QtGui.QCommandLinkButton(self.centralwidget)
        self.write_button.setMaximumSize(QtCore.QSize(150, 50))
        self.write_button.setObjectName("write_button")
        self.verticalLayout.addWidget(self.write_button)
        self.Received_button = QtGui.QCommandLinkButton(self.centralwidget)
        self.Received_button.setMaximumSize(QtCore.QSize(150, 50))
        self.Received_button.setObjectName("Received_button")
        self.verticalLayout.addWidget(self.Received_button)
        self.Sended_button = QtGui.QCommandLinkButton(self.centralwidget)
        self.Sended_button.setMaximumSize(QtCore.QSize(150, 50))
        self.Sended_button.setObjectName("Sended_button")
        self.verticalLayout.addWidget(self.Sended_button)
        self.Draft_button = QtGui.QCommandLinkButton(self.centralwidget)
        self.Draft_button.setMaximumSize(QtCore.QSize(150, 50))
        self.Draft_button.setObjectName("Draft_button")
        self.verticalLayout.addWidget(self.Draft_button)
        spacerItem = QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.Home = QtGui.QWidget()
        self.Home.setCursor(QtCore.Qt.ArrowCursor)
        self.Home.setObjectName("Home")
        self.tabWidget.addTab(self.Home, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 23))
        self.menubar.setObjectName("menubar")
        
        self.logout = QtGui.QAction('Log out', MainWindow)
        self.logout.setStatusTip('Log out')
        QtCore.QObject.connect(self.logout, QtCore.SIGNAL('triggered()'), self.logout_click)
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def logout_click(self):
        init.clear()
        sys.exit()
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.write_button.setText(QtGui.QApplication.translate("MainWindow", "Write Mail", None, QtGui.QApplication.UnicodeUTF8))
        self.Received_button.setText(QtGui.QApplication.translate("MainWindow", "Received", None, QtGui.QApplication.UnicodeUTF8))
        self.Sended_button.setText(QtGui.QApplication.translate("MainWindow", "Sended", None, QtGui.QApplication.UnicodeUTF8))
        self.Draft_button.setText(QtGui.QApplication.translate("MainWindow", "Draft", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), QtGui.QApplication.translate("MainWindow", "Home", None, QtGui.QApplication.UnicodeUTF8))

