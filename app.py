from flask import Flask
from flask_ngrok import run_with_ngrok
from fastapi import FastAPI
from twilio.rest import Client
import openai

# app = Flask(__name__)
# run_with_ngrok(app)

app = FastAPI()


# @app.route('/')
# def hello():
#     return "<h1>Hello World!</h1>"


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

openai.api_key = open_file('openaiapikey.txt')


@app.get('/')
def send_messages():
    account_sid="ACcbc9c8e7f5c625d1f9d620ec619478c9"
    auth_token="2052b26de4757bda70d04af215800112"
    from_number = "+13855267134"
    to_number = "+13474222198"
    client = Client(account_sid, auth_token)

    # GPT-3-Prompts
    prompt = "Hello there!How can i assist you today?"

    # Generate the response text using GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.5
    )
    response_text = response["choices"][0]['text'].strip()
    
    # Sending the message using Twilio
    message = client.messages.create(
        body=response_text,
        from_=from_number,
        to=to_number
    )

    context = {"message":"Message sent successfully!"}
    return context
    

if __name__ == "__main__":
    app.run()