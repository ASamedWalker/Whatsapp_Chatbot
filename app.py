import os
import openai
from flask import Flask, request
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello, World</h1>"


@app.route("/twilio/receiveMessage", methods=['POST'])
def receiveMessage():
    try:
        # Extract incoming  parameters from Twilio
        message = request.form['Body']
        sender_id = request.form['From']

        # Get response from openai
        result = text_complition(message)
        if result['status'] == 1:
            send_message(sender_id, result['response'])
    except:
        pass
    return 'OK', 200


openai.api_key = os.getenv('OPENAI_API_KEY')
def text_complition(prompt: str) -> dict:
    """
    Call Openai API

    Args:
        prompt (str): use query (str)

    Returns:
        dict: returns a dictionary
    """
    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=f'Human: {prompt}\nAI: ',
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }


account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)
def send_message(to: str, message: str) -> None:
    """_summary_

    Args:
        to (str): Sender of the message from +3474222198.
        message (str): text message to send

    Returns:
        -N
    """
    _ = client.messages.create(
        from_=os.getenv('FROM'),
        body=message,
        to=to
    )

if __name__=="__main__":
    app.run(debug=True)