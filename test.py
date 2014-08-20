import sys
from PyQt4 import QtCore, QtGui, QtWebKit
from version3 import Ui_MainWindow

from welcome import Ui_Welcome
from login import Ui_Login
from config import  Ui_Config
import init
import time
from Session import Session
from Mail import  MyMail
import email
class MyMailbox(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.Received_button, QtCore.SIGNAL("clicked()"), self.Received_button_click)
        QtCore.QObject.connect(self.ui.Sended_button, QtCore.SIGNAL("clicked()"), self.Sended_button_click)
        QtCore.QObject.connect(self.ui.write_button, QtCore.SIGNAL("clicked()"), self.write_button_click)
        QtCore.QObject.connect(self.ui.Draft_button, QtCore.SIGNAL("clicked()"), self.Draft_button_click)
        QtCore.QObject.connect(self.ui.tabWidget,QtCore.SIGNAL("tabCloseRequested(int)"),self.closeTab)
    
    
    def Received_button_click(self):
        self.ui.Received=self.pub_click("Received")
        if self.ui.Received!=None:
            self.ui.gridLayoutForReceived = QtGui.QGridLayout(self.ui.Received)
            self.ui.gridLayoutForReceived.setObjectName("gridLayoutForReceived")
            self.ui.verticalLayout_2 = QtGui.QVBoxLayout()
            self.ui.verticalLayout_2.setObjectName("verticalLayout_2")
            self.ui.tableWidget = QtGui.QTableWidget(self.ui.Received)
            self.ui.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            self.ui.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
            self.ui.tableWidget.setObjectName("tableWidget")
            self.ui.tableWidget.setColumnCount(4)
            self.ui.tableWidget.setRowCount(15)
            item = QtGui.QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            item.setText("Mark")
            self.ui.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            item.setText("From")
            self.ui.tableWidget.setHorizontalHeaderItem(1, item)
            item = QtGui.QTableWidgetItem()
            item.setText("Title")
            self.ui.tableWidget.setHorizontalHeaderItem(2, item)
            item = QtGui.QTableWidgetItem()
            item.setText("DateTime")
            self.ui.tableWidget.setHorizontalHeaderItem(3, item)
            self.ui.tableWidget.verticalHeader().setVisible(False)
            self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.ui.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
            self.ui.verticalLayout_2.addWidget(self.ui.tableWidget)
            self.ui.gridLayout = QtGui.QGridLayout()
            self.ui.gridLayout.setObjectName("gridLayout")
            spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            self.ui.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
            self.ui.horizontalLayout_4 = QtGui.QHBoxLayout()
            self.ui.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.ui.label = QtGui.QLabel(self.ui.Received)
            self.ui.label.setMinimumSize(QtCore.QSize(90, 30))
            self.ui.label.setMaximumSize(QtCore.QSize(90, 30))
            self.ui.label.setObjectName("label")
            self.ui.label.setText("Total Pages:")
            self.ui.horizontalLayout_4.addWidget(self.ui.label)
            self.ui.totalpagenum = QtGui.QLabel(self.ui.Received)
            self.ui.totalpagenum.setMaximumSize(QtCore.QSize(30, 30))
            self.ui.totalpagenum.setObjectName("totalpagenum")
            self.ui.horizontalLayout_4.addWidget(self.ui.totalpagenum)
            self.ui.label_3 = QtGui.QLabel(self.ui.Received)
            self.ui.label_3.setMinimumSize(QtCore.QSize(110, 30))
            self.ui.label_3.setMaximumSize(QtCore.QSize(110, 30))
            self.ui.label_3.setObjectName("label_3")
            self.ui.label_3.setText("Current Page:")
            self.ui.horizontalLayout_4.addWidget(self.ui.label_3)
            self.ui.currentpagenum = QtGui.QLabel(self.ui.Received)
            self.ui.currentpagenum.setMinimumSize(QtCore.QSize(30, 30))
            self.ui.currentpagenum.setObjectName("currentpagenum")
            self.ui.horizontalLayout_4.addWidget(self.ui.currentpagenum)
            self.ui.gridLayout.addLayout(self.ui.horizontalLayout_4, 0, 1, 1, 2)
            self.ui.horizontalLayout_5 = QtGui.QHBoxLayout()
            self.ui.horizontalLayout_5.setObjectName("horizontalLayout_5")
            self.ui.horizontalLayout_3 = QtGui.QHBoxLayout()
            self.ui.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.ui.backbutton = QtGui.QPushButton(self.ui.Received)
            self.ui.backbutton.setObjectName("backbutton")
            self.ui.backbutton.setText("Back")
            self.ui.horizontalLayout_3.addWidget(self.ui.backbutton)
            self.ui.nextbutton = QtGui.QPushButton(self.ui.Received)
            self.ui.nextbutton.setObjectName("nextbutton")
            self.ui.nextbutton.setText("Next")
            self.ui.horizontalLayout_3.addWidget(self.ui.nextbutton)
            self.ui.horizontalLayout_5.addLayout(self.ui.horizontalLayout_3)
            self.ui.horizontalLayout_2 = QtGui.QHBoxLayout()
            self.ui.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.ui.gotobutton = QtGui.QCommandLinkButton(self.ui.Received)
            self.ui.gotobutton.setMinimumSize(QtCore.QSize(120, 0))
            self.ui.gotobutton.setMaximumSize(QtCore.QSize(120, 16777215))
            self.ui.gotobutton.setObjectName("gotobutton")
            self.ui.gotobutton.setText("Go to page")
            self.ui.horizontalLayout_2.addWidget(self.ui.gotobutton)
            self.ui.whichpage = QtGui.QLineEdit(self.ui.Received)
            self.ui.whichpage.setMinimumSize(QtCore.QSize(30, 30))
            self.ui.whichpage.setMaximumSize(QtCore.QSize(30, 30))
            self.ui.whichpage.setText("")
            self.ui.whichpage.setObjectName("whichpage")
            self.ui.horizontalLayout_2.addWidget(self.ui.whichpage)
            self.ui.horizontalLayout_5.addLayout(self.ui.horizontalLayout_2)
            self.ui.gridLayout.addLayout(self.ui.horizontalLayout_5, 1, 0, 1, 2)
            spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            self.ui.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
            self.ui.verticalLayout_2.addLayout(self.ui.gridLayout)
            self.ui.gridLayoutForReceived.addLayout(self.ui.verticalLayout_2, 0, 0, 1, 1)
            self.initTable()
            self.received_currentpage=1
            self.received_pages=mail.getNumberOfPage()
            self.ui.totalpagenum.setText('%d'%self.received_pages)
            self.ui.currentpagenum.setText('%d'%self.received_currentpage)
            mailinfolist=mail.pop3_getMailHeadInfo(self.received_currentpage)
            self.showTableItems(mailinfolist)
            QtCore.QObject.connect(self.ui.backbutton,QtCore.SIGNAL("clicked()"),self.Back_button_click)
            QtCore.QObject.connect(self.ui.nextbutton,QtCore.SIGNAL("clicked()"),self.Next_button_click)
            QtCore.QObject.connect(self.ui.tableWidget, QtCore.SIGNAL("itemClicked (QTableWidgetItem*)"), self.getMailContent)
    def getMailContent(self, item):
        currentpage=str(self.ui.currentpagenum.text())
        currentpageNumber=int(currentpage)
        mailID=item.row()+(currentpageNumber-1)*15+1
        content=mail.retrMail(mailID)
        text=""
        for row in content:
            text=text+row+'\n'
        msg = email.message_from_string(text)
        mailcontent=""
        encode_type=""
        for par in msg.walk():
            if not par.is_multipart():
                content_type=par.get("content-type")
                start=content_type.find('charset=')
                if start!=-1:
                    encode_type=content_type[start+8:].strip("\'\"")
                else:
                    encode_type=""
                name = par.get_param("name") 
                if name:
                    h = email.Header.Header(name)
                    dh = email.Header.decode_header(h)
                    fname = dh[0][0]
                    print 'attach file name:', fname
                    data = par.get_payload(decode=True) 
                    
                    try:
                        f = open(fname, 'wb') 
                    except:
                        f = open('aaaa', 'wb')
                    f.write(data)
                    f.close()
                else:
                    if encode_type!="":
                        mailcontent =mailcontent+ par.get_payload(decode=True).decode(encode_type)
        
        newtab=QtGui.QWidget()
        self.ui.gridLayout_webview = QtGui.QGridLayout(newtab)
        self.ui.tabWidget.insertTab( self.ui.tabWidget.count(),newtab, item.text())
        webView = QtWebKit.QWebView(newtab)
        webView.setUrl(QtCore.QUrl("about:blank"))
        self.ui.gridLayout_webview.addWidget(webView, 0, 0, 1, 1)
        webView.setObjectName("webView")
        webView.setHtml(mailcontent)
    def initTable(self):
        for row in range(0, 15):
            for collum in range(0, 4):
                item=QtGui.QTableWidgetItem()
                self.ui.tableWidget.setItem(row, collum, item)
    def showTableItems(self, mails):
        i=0
        for info in mails:
            j=1
            for field in info:
                w=self.ui.tableWidget.item(i, j)
                w.setText(field)
                j=j+1
            i=i+1
        if(len(mails)<15):
            for i in range(len(mails), 15):
                for j in range(1, 4):
                    w=self.ui.tableWidget.item(i, j)
                    w.setText('')
    def Back_button_click(self):
        if(self.received_currentpage==1):
            return
        else:
            self.received_currentpage=self.received_currentpage-1
            self.ui.currentpagenum.setText('%d'%self.received_currentpage)
            mailinfolist=mail.pop3_getMailHeadInfo(self.received_currentpage)
            self.showTableItems(mailinfolist)
    def Next_button_click(self):
        if(self.received_currentpage==self.received_pages):
            return
        else:
            self.received_currentpage=self.received_currentpage+1
            self.ui.currentpagenum.setText('%d'%self.received_currentpage)
            mailinfolist=mail.pop3_getMailHeadInfo(self.received_currentpage)
            self.showTableItems(mailinfolist)
    def Sended_button_click(self):
        self.ui.Sended=self.pub_click("Sended")
        if self.ui.Sended!=None:
            self.ui.gridLayoutForSended = QtGui.QGridLayout(self.ui.Sended)
            self.ui.gridLayoutForSended.setObjectName("gridLayoutForSended")
            self.ui.verticalLayout_2_sended = QtGui.QVBoxLayout()
            self.ui.verticalLayout_2_sended.setObjectName("verticalLayout_2_sended")
            self.ui.tableWidget_sended = QtGui.QTableWidget(self.ui.Sended)
            self.ui.tableWidget_sended.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            self.ui.tableWidget_sended.setGridStyle(QtCore.Qt.SolidLine)
            self.ui.tableWidget_sended.setObjectName("tableWidget_sended")
            self.ui.tableWidget_sended.setColumnCount(4)
            self.ui.tableWidget_sended.setRowCount(15)
            item = QtGui.QTableWidgetItem()
            self.ui.tableWidget_sended.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            item.setText("Mark")
            self.ui.tableWidget_sended.setHorizontalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            item.setText("To")
            self.ui.tableWidget_sended.setHorizontalHeaderItem(1, item)
            item = QtGui.QTableWidgetItem()
            item.setText("Title")
            self.ui.tableWidget_sended.setHorizontalHeaderItem(2, item)
            item = QtGui.QTableWidgetItem()
            item.setText("DateTime")
            self.ui.tableWidget_sended.setHorizontalHeaderItem(3, item)
            self.ui.tableWidget_sended.verticalHeader().setVisible(False)
            self.ui.tableWidget_sended.horizontalHeader().setStretchLastSection(True)
            self.ui.verticalLayout_2_sended.addWidget(self.ui.tableWidget_sended)
            self.ui.gridLayout_sended = QtGui.QGridLayout()
            self.ui.gridLayout_sended.setObjectName("gridLayout")
            spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            self.ui.gridLayout_sended.addItem(spacerItem4, 0, 0, 1, 1)
            self.ui.horizontalLayout_4_sended = QtGui.QHBoxLayout()
            self.ui.horizontalLayout_4_sended.setObjectName("horizontalLayout_4")
            self.ui.label_sended = QtGui.QLabel(self.ui.Sended)
            self.ui.label_sended.setMinimumSize(QtCore.QSize(90, 30))
            self.ui.label_sended.setMaximumSize(QtCore.QSize(90, 30))
            self.ui.label_sended.setObjectName("label_sended")
            self.ui.label_sended.setText("Total Pages:")
            self.ui.horizontalLayout_4_sended.addWidget(self.ui.label_sended)
            self.ui.totalpagenum_sended = QtGui.QLabel(self.ui.Sended)
            self.ui.totalpagenum_sended.setMaximumSize(QtCore.QSize(30, 30))
            self.ui.totalpagenum_sended.setObjectName("totalpagenum_sended")
            self.ui.horizontalLayout_4_sended.addWidget(self.ui.totalpagenum_sended)
            self.ui.label_3_sended = QtGui.QLabel(self.ui.Sended)
            self.ui.label_3_sended.setMinimumSize(QtCore.QSize(110, 30))
            self.ui.label_3_sended.setMaximumSize(QtCore.QSize(110, 30))
            self.ui.label_3_sended.setObjectName("label_3_sended")
            self.ui.label_3_sended.setText("Current Page:")
            self.ui.horizontalLayout_4_sended.addWidget(self.ui.label_3_sended)
            self.ui.currentpagenum_sended = QtGui.QLabel(self.ui.Sended)
            self.ui.currentpagenum_sended.setMinimumSize(QtCore.QSize(30, 30))
            self.ui.currentpagenum_sended.setObjectName("currentpagenum_sended")
            self.ui.horizontalLayout_4_sended.addWidget(self.ui.currentpagenum_sended)
            self.ui.gridLayout_sended.addLayout(self.ui.horizontalLayout_4_sended, 0, 1, 1, 2)
            self.ui.horizontalLayout_5_sended = QtGui.QHBoxLayout()
            self.ui.horizontalLayout_5_sended.setObjectName("horizontalLayout_5_sended")
            self.ui.horizontalLayout_3_sended = QtGui.QHBoxLayout()
            self.ui.horizontalLayout_3_sended.setObjectName("horizontalLayout_3_sended")
            self.ui.backbutton_sended = QtGui.QPushButton(self.ui.Sended)
            self.ui.backbutton_sended.setObjectName("backbutton_sended")
            self.ui.backbutton_sended.setText("Back")
            self.ui.horizontalLayout_3_sended.addWidget(self.ui.backbutton_sended)
            self.ui.nextbutton_sended = QtGui.QPushButton(self.ui.Sended)
            self.ui.nextbutton_sended.setObjectName("nextbutton_sended")
            self.ui.nextbutton_sended.setText("Next")
            self.ui.horizontalLayout_3_sended.addWidget(self.ui.nextbutton_sended)
            self.ui.horizontalLayout_5_sended.addLayout(self.ui.horizontalLayout_3_sended)
            self.ui.horizontalLayout_2_sended = QtGui.QHBoxLayout()
            self.ui.horizontalLayout_2_sended.setObjectName("horizontalLayout_2_sended")
            self.ui.gotobutton_sended = QtGui.QCommandLinkButton(self.ui.Sended)
            self.ui.gotobutton_sended.setMinimumSize(QtCore.QSize(120, 0))
            self.ui.gotobutton_sended.setMaximumSize(QtCore.QSize(120, 16777215))
            self.ui.gotobutton_sended.setObjectName("gotobutton_sended")
            self.ui.gotobutton_sended.setText("Go to page")
            self.ui.horizontalLayout_2_sended.addWidget(self.ui.gotobutton_sended)
            self.ui.whichpage_sended = QtGui.QLineEdit(self.ui.Sended)
            self.ui.whichpage_sended.setMinimumSize(QtCore.QSize(30, 30))
            self.ui.whichpage_sended.setMaximumSize(QtCore.QSize(30, 30))
            self.ui.whichpage_sended.setText("")
            self.ui.whichpage_sended.setObjectName("whichpage_sended")
            self.ui.horizontalLayout_2_sended.addWidget(self.ui.whichpage_sended)
            self.ui.horizontalLayout_5_sended.addLayout(self.ui.horizontalLayout_2_sended)
            self.ui.gridLayout_sended.addLayout(self.ui.horizontalLayout_5_sended, 1, 0, 1, 2)
            spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            self.ui.gridLayout_sended.addItem(spacerItem5, 1, 2, 1, 1)
            self.ui.verticalLayout_2_sended.addLayout(self.ui.gridLayout_sended)
            self.ui.gridLayoutForSended.addLayout(self.ui.verticalLayout_2_sended, 0, 0, 1, 1)
    def Draft_button_click(self):
        self.pub_click("Draft")
        
    
     
    def write_button_click(self): 
        self.ui.NewMail=self.pub_click("NewMail")
        if self.ui.NewMail != None :
            self.ui.gridLayoutForNewMail = QtGui.QGridLayout(self.ui.NewMail)
            self.ui.verticalLayoutForMailPanel = QtGui.QVBoxLayout()
            self.ui.header = QtGui.QGridLayout()
            self.ui.label = QtGui.QLabel(self.ui.NewMail)
            self.ui.label.setText("Send To :")
            self.ui.header.addWidget(self.ui.label, 0, 0, 1, 1)
            self.ui.lineEdit = QtGui.QLineEdit(self.ui.NewMail)
            self.ui.lineEdit.setObjectName("lineEdit")
            self.ui.header.addWidget(self.ui.lineEdit, 0, 1, 1, 1)
            self.ui.label_2 = QtGui.QLabel(self.ui.NewMail)
            self.ui.label_2.setObjectName("title")
            self.ui.label_2.setText("Tile :")
            self.ui.header.addWidget(self.ui.label_2, 1, 0, 1, 1)
            self.ui.lineEdit_2 = QtGui.QLineEdit(self.ui.NewMail)
            self.ui.lineEdit_2.setObjectName("lineEdit_2")
            self.ui.header.addWidget(self.ui.lineEdit_2, 1, 1, 1, 1)
            self.ui.verticalLayoutForMailPanel.addLayout(self.ui.header)
            self.ui.file_to_send = QtGui.QLabel(self.ui.NewMail)
            self.ui.file_to_send.setObjectName("file_to_send")
            self.ui.file_to_send.setText("File To Send :")
            self.ui.verticalLayoutForMailPanel.addWidget(self.ui.file_to_send)
            self.ui.content = QtGui.QVBoxLayout()
            self.ui.content.setObjectName("content")
            self.ui.label_4 = QtGui.QLabel(self.ui.NewMail)
            self.ui.label_4.setObjectName("label_4")
            self.ui.label_4.setText("Content : ")
            self.ui.content.addWidget(self.ui.label_4)
            self.ui.textEdit = QtGui.QTextEdit(self.ui.NewMail)
            self.ui.textEdit.setMinimumSize(QtCore.QSize(0, 0))
            self.ui.textEdit.setObjectName("textEdit")
            self.ui.content.addWidget(self.ui.textEdit)
            self.ui.send = QtGui.QPushButton(self.ui.NewMail)
            self.ui.send.setObjectName("send")
            self.ui.send.setText("Send")
            self.ui.content.addWidget(self.ui.send)
            self.ui.verticalLayoutForMailPanel.addLayout(self.ui.content)
            self.ui.gridLayoutForNewMail.addLayout(self.ui.verticalLayoutForMailPanel, 0, 0, 1, 1)
            QtCore.QObject.connect(self.ui.send,QtCore.SIGNAL("clicked()"),self.Send_button_click)
    def Send_button_click(self):
        global mail
        global session
        fro=session.userName
        to=str(self.ui.lineEdit.text()).split(';')
        subject=str(self.ui.lineEdit_2.text())
        text=str(self.ui.textEdit.toPlainText())
        mail.smtp_send(fro, to, subject, text)
    def closeTab(self, index):
        self.ui.tabWidget.removeTab(index) 
        
   
    def pub_click(self, text):
        count = self.ui.tabWidget.count()
        flag = False
        tab=QtGui.QWidget()
        for i in range(0, count) :
            tab=self.ui.tabWidget.widget(i)
            tab_name=tab.objectName()
            if tab_name.compare(text, QtCore.Qt.CaseSensitive)  == 0 :
                flag = True
                break;
        if  flag == False :
             pub_tab=QtGui.QWidget()
             pub_tab.setObjectName(text);
             self.ui.tabWidget.insertTab(count,pub_tab, text)
             self.ui.tabWidget.setCurrentWidget(pub_tab)
             return pub_tab
        else :
            self.ui.tabWidget.setCurrentWidget(tab)
            return None
class  LoginWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.button_click)
    def button_click(self):
        global configWin
        global session
        global myapp
        global mail
        pop3Name=str(configWin.ui.lineEdit.text())
        smtpName=str(configWin.ui.lineEdit_2.text())
        userName=str(self.ui.lineEdit.text())
        passwd=str(self.ui.lineEdit_2.text())
        session=Session([pop3Name, smtpName, userName, passwd])
        resultcode=session.sessionLogin()
        if resultcode==0:
            lastaccount=[pop3Name, smtpName, userName, passwd]
            init.writein(lastaccount)
            mail=MyMail(session)
            myapp = MyMailBox()
            myapp.show()
            myapp.ui.menubar.addMenu(lastaccount[2]).addAction(myapp.ui.logout)
            self.close()
class  ConfigWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Config()
        self.ui.setupUi (self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.button_click)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.button2_click)
        
    def button_click(self):
        global loginWin
        if str(self.ui.lineEdit.text())!="" and str(self.ui.lineEdit_2.text())!="" :
            loginWin=LoginWindow()
            loginWin.show()
            self.close()
    def button2_click(self):
        global welcomeWin
        welcomeWin=WelcomeWindow()
        welcomeWin.show()
        self.close()
        
class  WelcomeWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui=Ui_Welcome()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.button_click)
    def button_click(self):
        global configWin
        configWin=ConfigWindow()
        configWin.show()
        self.close()

configWin=None
loginWin=None
welcomeWin=None
session=None
myapp=None
mail=None
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    if init.IsFirstUse():
        welcomeWin=WelcomeWindow()
        welcomeWin.show()
    else:
        myapp = MyMailBox()
        lastaccount=init.load()
        session=Session(lastaccount)
        resultcode=session.sessionLogin()
        if resultcode==0:
            mail=MyMail(session)
            myapp.show()
            myapp.ui.menubar.addMenu(lastaccount[2]).addAction(myapp.ui.logout)
    sys.exit(app.exec_())
