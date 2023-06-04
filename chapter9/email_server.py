import smtplib

from email.mime.text import MIMEText

body='This is the body of a test mail.\n This mail is sent via a python program'

msg=MIMEText(body)

fromaddr = ""
toaddr=""

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Test Mail'

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr, '')

server.send_message(msg)
print('Mail Sent')
server.quit()
