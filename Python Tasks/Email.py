import pywhatkit as pw
sender_email = input("Enter your Gmail address: ")
app_password = input("Enter your Gmail app password: ")
subject = input("Enter the subject of the email: ")
message = input("Enter the message to send: ")
receiver_email = input("Enter the receiver's email address: ")
pw.send_mail(sender_email, app_password, subject, message, receiver_email)
