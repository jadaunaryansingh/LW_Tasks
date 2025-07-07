import os
from twilio.rest import Client
account_sid =input("Please enter your SID")
acc_token = input("Please enter token")
client = Client(account_sid, acc_token)
call = client.calls.create(
    twiml='<Response><Say>Hi, this is a Python call</Say></Response>',
    to=int(input("Receiver Number")),
    from_=int(input("Sender's Number"))
)
print (call.sid)
