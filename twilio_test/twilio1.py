# One way WhatsApp message - Order Notifications #

# first, 'pip3 install twilio'
from twilio.rest import Client

# this needs to be exported
account_sid = 'ACd438cd43a6cbd146c97c5fb92615df4f'
# this needs to be exported
auth_token = 'ceb90e924ce88f05715c4154ec758549'

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Your Verdis AI order of 1 smart solution has shipped and should be delivered on July 10, 2019. Details: vpractice.ai/',
    to='whatsapp:+919044099200'
)

print(message.sid)
