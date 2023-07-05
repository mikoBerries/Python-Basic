# simple mail transfer proctol used lib -> smtplib
# logic of code similar lik simple bank project send email
import smtplib

# using gmail SMTP
smtp_object = smtplib.SMTP('smtp.gmail.com',587)

smtp_object.ehlo()
smtp_object.starttls()

# For hidden passwords
import getpass
# getting password for gmail apps password
result = getpass.getpass("Type something here and it will be hidden: ")

# sensitif data must save in env server (more secure and not naked like this)

# logging to google smtp
email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your password: ")
smtp_object.login(email,password)

# build your email pattern
from_address = getpass.getpass("Enter your email: ")
to_address = getpass.getpass("Enter the email of the recipient: ")
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address,to_address,msg)

# run this code while server are shutingdown / already not using smtp again
smtp_object.quit()