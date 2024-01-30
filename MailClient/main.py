import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from config import settings

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(settings.sender_email, settings.password)

msg = MIMEMultipart()

msg['From'] = 'Wali yar'
msg['To'] = settings.reciever_email
msg['Subject'] = 'Testing'

msg.attach(MIMEText('Hello World!', 'plain'))

filename = r"C:\Users\YarKhan\Documents\Anime\Master.jpeg"
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content Disposition', f'attachement; filename = {filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail(settings.sender_email, settings.reciever_email, text)

server.quit()