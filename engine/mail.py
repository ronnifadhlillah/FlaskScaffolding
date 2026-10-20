from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import smtplib
import configparser

cfg=configparser.ConfigParser()
cfg.read("config/app.py")

def mailConfig(subject,body,recipient,bcc=None):
  sendMail=cfg["Mail"]["Username"]
  reciMail=recipient
  smtpServer=cfg["Mail"]["Smtp"]
  smtpPort=cfg["Mail"]["Port"]
  smtpUsername=cfg["Mail"]["Username"]
  smtpPassword=cfg["Mail"]["Password"]
  msg=MIMEMultipart()
  msg["from"]=formataddr((cfg["Mail"]["masking"],sendMail))
  msg["to"]=formataddr((cfg["Mail"]["masking"],sendMail))
  msg["bcc"]=formataddr((cfg["Mail"]["masking"],sendMail))

  msg["subject"]=subject
  msg.attach(MIMEText(body,"html"))

  with smtplib.SMTP_SSL(smtpServer,smtpPort) as srv:
    srv.login(smtpUsername,smtpPassword)
    srv.sendmail(sendMail,reciMail,msg.as_string())

def attachment