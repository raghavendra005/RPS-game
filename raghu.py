#sending email

import smtplib

sender = "sendermail.com"
receiver = "receivermail.com"
password = "<password>"
subject = "Security Alert!"
body = "Your account is hacked!"


#header----------------------------
message = f""" From : {sender}
TO : {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com" , 587)  #587 is the default port to send mail
server.starttls()


server.login(sender,password)
print("Logged in!")
server.sendmail(sender,receiver,message)
print("Email has been sent!")

