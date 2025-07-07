from twilio.rest import Client
account_sid = input("Please enter your SID: ")
auth_token = input("Please enter your token: ")
client = Client(account_sid, auth_token)
to_number = input("Receiver Number (with country code, e.g. +911234567890): ")
from_number = input("Sender's Twilio Number (e.g. +1415XXXXXXX): ")
message = client.messages.create(
    body="Hi, this is a Python SMS",
    to=to_number,
    from_=from_number
)
print("Message Status:", message.status)
