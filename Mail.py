
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

# python 2.3.*: email.Utils email.Encoders
from email.utils import COMMASPACE,formatdate
from email import encoders
from email.header import decode_header
import os
import re
class MyMail:
    def __init__(self, session):
        self.pop=session.pop
        self.smtp=session.smtp
    def  smtp_send(self, fro, to, subject, text, files=[]):
        assert type(to) == list 
        assert type(files) == list 
    
        msg = MIMEMultipart() 
        msg['From']=fro
        msg['To']=COMMASPACE.join(to)
        msg['Date'] = formatdate(localtime=True) 
        msg['Subject'] = subject 
        msg.attach(MIMEText(text))
    
        for file in files : 
            part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data 
            part.set_payload(open(file, 'rb'.read())) 
            encoders.encode_base64(part) 
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file)) 
            msg.attach(part) 
    
        self.smtp.sendmail(fro, to, msg.as_string()) 
    
    def getNumberOfPage(self):
        stat =self.pop.stat()
        if(stat[0]%15==0):
            return stat[0]/15
        else:
            return stat[0]/15+1
        
    def pop3_getMailHeadInfo(self, page):
        mailInfoList=[]
        mailInfo=()
        stat =self.pop.stat()
        if(stat[0]-(page-1)*15<15):
            startitem=(page-1)*15+1
            enditem=(page-1)*15+1+stat[0]-(page-1)*15
        else:
            startitem=(page-1)*15+1
            enditem=startitem+15
        for i in range(startitem, enditem):
            headinfos= self.pop.top(i, 0)
            infos=headinfos[1]
            fro=''
            subject=''
            date=''
            
            for j in range(0, len(infos)):
                info=infos[j]
                k=j+1
                if info.find("From")==0:
                    start=info.find(':')
                    
                    part=info[start+1: ]
                    part=part.translate(None, '"')
                    
                    part=part.replace('<', ' <')
                    if k==len(infos):
                        info=part
                        froinfo=decode_header(info)
                        fro=self.getContent(froinfo)
                        continue
                    pattern = re.compile(r'^[A-Z].{,30}: .*$')
                    match=pattern.match(infos[k])
                   
                    while match==None:
                        part=part+infos[k]
                        k=k+1
                        if k==len(infos):
                            break
                        match=pattern.match(infos[k])
                    info=part
                    froinfo=decode_header(info)
                    fro=self.getContent(froinfo)
                    continue
                elif info.find("Subject")==0:
                    start=info.find(':')
                    part=info[start+1: ]
                    if k==len(infos):
                        info=part
                        subjectinfo=decode_header(info)
                        subject=self.getContent(subjectinfo);
                        continue
                    pattern = re.compile(r'^[A-Z].{,30}: .*$')
                    match=pattern.match(infos[j+1])
                    while match==None:
                        part=part+infos[k]
                        k=k+1
                        if k==len(infos):
                            break
                        match=pattern.match(infos[k])
                    info=part
                    subjectinfo=decode_header(info)
                    subject=self.getContent(subjectinfo);
                    continue
                elif info.find("Date")==0:
                    start=info.find(':')
                    part=info[start+1: ]
                    if k==len(infos):
                        info=part
                        dateinfo=decode_header(info)
                        date=self.getContent(dateinfo)
                        continue
                    pattern = re.compile(r'^[A-Z].{,30}: .*$')
                    match=pattern.match(infos[j+1])
                    while match==None:
                        part=part+infos[k]
                        k=k+1
                        if k==len(infos):
                            break
                        match=pattern.match(infos[k])
                    info=part
                    dateinfo=decode_header(info)
                    date=self.getContent(dateinfo)
            mailInfo=(fro, subject, date)
            mailInfoList.append(mailInfo)
        return mailInfoList
    

    def getContent(self, infos):
        content=""
        for item in infos:
            if  item[1]!=None:
                content+=item[0].decode(item[1])
            else:
                content+=item[0]
        return content   
    def retrMail(self, id):
        content=self.pop.retr(id)[1]
        return content
