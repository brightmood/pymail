import poplib
import smtplib

class  Session: 
    def __init__(self, list):
        self.pop3Name=list[0]
        self.smtpName=list[1]
        self.userName=list[2]
        self.passwd=list[3]
    def sessionLogin(self):
        try:
            self.smtp = smtplib.SMTP(self.smtpName) 
        except Exception , e :
            print e
            return 1
        try:
            self.smtp.login(self.userName, self.passwd)
        except Exception , e :
            print e
            return 2
        
        try:
            self.pop=poplib.POP3(self.pop3Name)
        except Exception ,  e:
            print e
            return 3
        try:
            self.pop.set_debuglevel(1)
            self.pop.user(self.userName)
            self.pop.pass_(self.passwd)
        except Exception ,  e:
            print e
            return 4
        self.isLogin=True
        return 0
    def sessionLogout(self):
        if self.isLogin:
            self.pop.quit()
            self.smtp.close()
        
