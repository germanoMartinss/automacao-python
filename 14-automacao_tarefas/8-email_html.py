from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

password = open('senha', 'r').read()

from_email = 'germanoicloud1991@gmail.com'
to_email = 'germanopmartins91@gmail.com'
subject = 'Proposta de trabalho customizada'
body = open('files/index.html.txt', 'r', encoding='utf-8').read()

msg = EmailMessage()

msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email

msg.set_content(body, subtype='html')

safe = ssl.create_default_context()

# 2 - Adicionar anexos 

anexo = 'files/corpo.txt'
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as ap:
    msg.add_attachment(
        ap.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(from_email, to_email, msg.as_string())