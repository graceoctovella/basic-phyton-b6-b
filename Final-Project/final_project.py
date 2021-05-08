import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

senderaddr = "graceoctovella@gmail.com"
receiveraddr = open("receiver_list.txt", "r")
toaddr = receiveraddr.readlines()

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
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderaddr, "password")
text = msg.as_string()
server.sendmail(senderaddr, toaddr, text)
server.quit()