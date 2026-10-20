from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import formataddr
from email import encoders
import smtplib
import configparser
import os

cfg=configparser.ConfigParser()
cfg.read("config/app.py")

def mailConfig(subject,body,recipient,bcc=None,attach=None):
  sendMail=cfg["Mail"]["Username"]
  reciMail=recipient
  smtpServer=cfg["Mail"]["Smtp"]
  smtpPort=cfg["Mail"]["Port"]
  smtpUsername=cfg["Mail"]["Username"]
  smtpPassword=cfg["Mail"]["Password"]
  msg=MIMEMultipart()
  msg["from"]=formataddr((cfg["Mail"]["masking"],sendMail))
  msg["to"]=formataddr((cfg["Mail"]["masking"],sendMail))
  if bcc is not None:
    msg["bcc"]=formataddr((cfg["Mail"]["masking"],sendMail))

  if attach is not None:
    attachment(attach)
    msg.attach(part)

  msg["subject"]=subject
  msg.attach(MIMEText(body,"html"))

  with smtplib.SMTP_SSL(smtpServer,smtpPort) as srv:
    srv.login(smtpUsername,smtpPassword)
    srv.sendmail(sendMail,reciMail,msg.as_string())

def attachment(fp):
  if fp and os.path.exists(fp):
    fn=os.path.basename(fp)

  with open(fp,"rb") as attachment:
    part=MIMEBase("Application","octet-stream")
    part.st_payload(attachment.read())

  encoders.encode_base64(part)

  part.add_header("content-disposition",f"attachment;filename={fn}")

  
    