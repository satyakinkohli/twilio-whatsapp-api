# One way WhatsApp message - Order Notifications #

# first, 'pip3 install twilio'
from twilio.rest import Client
import config

# account_sid needs to be exported in the env using the following command
# export account_sid=abcdef
account_sid = config.account_sid
# auth_token needs to be exported in the env using the following command
# export auth_token=lmnopq
auth_token = config.auth_token

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Your Verdis AI order of 1 smart solution has shipped and should be delivered on July 10, 2019. Details: vpractice.ai/',
    to='whatsapp:+919044099200'
)

print(message.sid)
