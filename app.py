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
    m_cont = request.form.get("Body").lower()

    # # INTELLIGENT BOT # #
    # # Reply to the message
    m_resp = MessagingResponse()
    if m_cont == 'hello':
        # m_resp.message("Hello to you too. How are you?")
        m_resp.message().body("Hello to you too. How are you?")
    elif m_cont == 'random number':
        m_resp.message().body("A random number for you is " + str(random.randint(0, 100)) + ".")
        m_resp.message().media('https://bit.ly/3hf3oEx')
    else:
        m_resp.message().body("You have asked me to do something which is beyond my capabilities at the moment.")

    # # ECHO BOT # #
    # # Reply to the message
    # m_resp = MessagingResponse()
    # m_resp.message().body("You said: {}".format(m_cont))

    return str(m_resp)


if __name__ == "__main__":
    app.run(debug=True)
