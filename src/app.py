from helper.openai_api import text_complition
from helper.twilio_api import send_message


from flask import Flask, request
# from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
# app = FastAPI()


@app.route("/")
def home():
    return "<h1>Hello, World</h1>"


@app.route("/twilio/receiveMessage", methods=["POST"])
def receiveMessage():
    try:
        # Extract incoming  parameters from Twilio
        message = request.form["Body"]
        sender_id = request.form["From"]

        # Get response from openai
        result = text_complition(message)
        if result["status"] == 1:
            send_message(sender_id, result["response"])
    except FileExistsError:
        pass
    return "OK", 200



