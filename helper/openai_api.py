import os
import openai

from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")


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
            model="text-davinci-003",
            prompt=f"Human: {prompt}\nAI: ",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["Human:", "AI:"],
        )
        return {"status": 1, "response": response["choices"][0]["text"]}
    except FileExistsError:
        return {"status": 0, "response": ""}
