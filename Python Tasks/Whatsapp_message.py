import pywhatkit as pw
phone = input("Enter receiver's phone number with country code (e.g., +91xxxxxxxxxx): ")
message = input("Enter the message to send: ")
hour = int(input("Enter hour (24-hour format): "))
minute = int(input("Enter minute: "))
pw.sendwhatmsg(phone, message, hour, minute)
