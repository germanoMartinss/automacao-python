from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import ssl

password = open('senha', 'r').read()
# print(password)

from_email = 'germanoicloud1991@gmail.com'
to_email = 'germanopmartins91@gmail.com'
subject = 'Teste de envio de email'
body = 'Olá, tudo bem?'

msg = EmailMessage()

msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email

msg.set_content(body)

safe = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(from_email, to_email, msg.as_string())

