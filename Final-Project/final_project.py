import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

senderaddr = "graceoctovella@gmail.com"
toaddr = []
with open("receiver_list.txt", "r") as email:
    emails = email.readlines()
    for all_mail in emails:
        toaddr.append(all_mail.strip("\n"))

msg = MIMEMultipart()
msg['From'] = senderaddr
msg['To'] = ",".join(toaddr)
msg['Subject'] = "Greetings from Jogja"

body = "Hello World, I am Anya from Jogja. I hope someday I can travel around to meet you."
msg.attach(MIMEText(body, 'plain'))

filename = "tugujogja.jpg"
attachment = open("C:\\Users\\ACER\\Pictures\\tugujogja.jpg", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename = %s" % filename)
 
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderaddr, "graceanakugm28")
text = msg.as_string()
server.sendmail(senderaddr, toaddr, text)
server.quit()

#https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/
#https://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib
#https://www.kite.com/python/answers/how-to-read-a-text-file-into-a-list-in-python
#https://stackoverflow.com/questions/7232088/python-subject-not-shown-when-sending-email-using-smtplib-module
