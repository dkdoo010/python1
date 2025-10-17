import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject']='파일첨부 예제'
msg['FROM'] = EMAIL_ADDRESS
msg['TO'] = 'dsaasdas351@gmail.com'
msg.set_content('파일을 첨부합니다')
# smtp.send_message(msg)

with open('manage3.png', 'rb') as file:
    msg.add_attachment(file.read(), maintype='image', 
                       subtype='png', filename=file.name)

with open('sample.xlsx', 'rb') as file:
    msg.add_attachment(file.read(), maintype='application', 
                       subtype='octect-stream', filename=file.name)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)
    smtp.send_message(msg)