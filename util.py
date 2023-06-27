import openai
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPEN_API2", "NONE")

Initial_content = " "

def initial_message():
    messages = [
        {"role": "system",
            "content": f"{Initial_content}"},
            {"role": "user", "content": "Can i talk to you?"},
            {"role": "assistant", "content": "Hi, I am here to to listen to you. Please speak"}
    ]
    return messages

def get_response(messages, model="gpt-3.5-turbo"):
    print("model: ", model)
    response = openai.ChatCompletion.create(model=model,
                                     messages=messages,
                                     )
    return response['choices'][0]['message']['content']

def update_message(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
