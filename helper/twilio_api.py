import os
from twilio.rest import Client

from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)


def send_message(to: str, message: str) -> None:
    """_summary_

    Args:
        to (str): Sender of the message from +3474222198.
        message (str): text message to send

    Returns:
        -N
    """
    _ = client.messages.create(from_=os.getenv("FROM"), body=message, to=to)
