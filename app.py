import smtplib

sender_email = "sender@gmail.com"
password = "password"
receiver_email = "receiver@gmail.com"
message = "Hey, How are you ?"
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender_email,password)
server.sendmail(sender_email, receiver_email, message)
print('Mail Successfully Sent!')
server.quit()
