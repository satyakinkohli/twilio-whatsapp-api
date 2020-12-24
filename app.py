from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

import random

app = Flask(__name__)


@app.route("/")
def hello():
    return "Testing of Twilio WhatsApp Bot is going on. Please come back later!"


@app.route("/sms", methods=["POST"])
def sms_reply():

    # Fetch the message sent by the user
    msg_in = request.form.get("Body").lower()

    # # INTELLIGENT BOT # #
    # # Reply to the message
    msg_out = MessagingResponse()
    if msg_in == 'hello':
        # msg_out.message("Hello to you too. How are you?")
        msg_out.message().body("Hello to you too. How are you?")
    elif msg_in == 'random number':
        msg_out.message().body("A random number for you is " + str(random.randint(0, 100)) + ".")
        msg_out.message().media('https://bit.ly/3hf3oEx')
    else:
        msg_out.message().body("You have asked me to do something which is beyond my capabilities at the moment.")

    # # ECHO BOT # #
    # # Reply to the message
    # msg_out = MessagingResponse()
    # msg_out.message().body("You said: {}".format(msg_in))

    return str(msg_out)


if __name__ == "__main__":
    app.run(debug=True)
