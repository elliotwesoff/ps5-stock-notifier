from twilio.rest import Client

account_sid = None
auth_token = None
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='',
    body='hello this is a test',
    to='+16262727059'
)

print(message.sid)
