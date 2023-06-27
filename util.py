import openai
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPEN_API2", "NONE")

Initial_content = ""

def initial_message() -> list:
    messages = [
        {"role": "system",
            "content": f"{Initial_content}"},
            {"role": "user", "content": "Can i talk to you?"},
            {"role": "assistant", "content": "Hi, I am here to to listen to you. Please speak"}
    ]
    return messages

def get_response(messages:list, model:str="gpt-3.5-turbo") -> str:
    """
    Get the response from the language model for a given conversation.

    Args:
        messages (list): A list of messages representing the conversation.
        model (str, optional): The model to use for generating the response. Defaults to "gpt-3.5-turbo".

    Returns:
        str: The generated response from the language model.
    """
    print("model: ", model)
    response = openai.ChatCompletion.create(model=model,
                                     messages=messages,
                                     )
    return response['choices'][0]['message']['content']

def update_message(messages:list, role:str, content:str) -> list:
    """
    Add a new message to the conversation.

    Args:
        messages (list): A list of messages representing the conversation.
        role (str): The role of the message (e.g., "user", "assistant").
        content (str): The content of the message.

    Returns:
        list: The updated list of messages.
    """
    messages.append({"role": role, "content": content})
    return messages
