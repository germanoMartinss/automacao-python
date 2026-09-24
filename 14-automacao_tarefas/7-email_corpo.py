from email.message import EmailMessage
import smtplib
import ssl

password = open('senha', 'r').read()

from_email = 'germanoicloud1991@gmail.com'
to_email = 'germanopmartins91@gmail.com'
subject = 'Proposta de trabalho'
body = open('files/corpo.txt', 'r', encoding='utf-8').read()

msg = EmailMessage()

msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email

msg.set_content(body)

safe = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(from_email, to_email, msg.as_string())