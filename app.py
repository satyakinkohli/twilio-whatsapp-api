from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/")
def hello():
    return "Testing of Twilio WhatsApp Bot is going on. Please come back later!"


@app.route("/sms", methods=["POST"])
def sms_reply():
    # Fetch the message sent by the user
    message_content = request.form.get("Body")

    message_response = ''
    if message_content == 'Hello':
        message_response = MessagingResponse()
        message_response.message("Hello to you too. How are you?")
    elif message_content == 'birthday':
        message_response = MessagingResponse()
        message_response.message("Happy Birthday genius")

    # # Reply to the message
    # message_response = MessagingResponse()
    # message_response.message("You said: {}" .format(message_content))

    return str(message_response)


if __name__ == "__main__":
    app.run(debug=True)
