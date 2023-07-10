import openai
from dotenv import load_dotenv, find_dotenv
import os
import psycopg2
import streamlit as st
from datetime import datetime

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPEN_API2", "NONE")


def initial_message():
    messages = [
        {"role": "system",
            "content": """You are a mental health human bot whose purpose is to act as a 
                         companion to people and maintain a conversationa that helps to collect enough data. 
                         Maintain a converstaion that ecourages people to speak about what they go through.
                         You can tell short stories or sceneriors to make it very conversatinanl. 
                         Just make sure to keep the conversation unless the user explicitely says its over.  
                         Dont keep asking questions everytime. 
                         Make it as converssational as possible. Make them feel comfortable for speaking with you. 
                         Be as human as you can"""},
            {"role": "user", "content": "Can i talk to you?"},
            {"role": "assistant", "content": "Hi, I am here to to listen to you. Please speak"}
    ]
    return messages

@st.cache_data()
def get_response(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(model=model,
                                     messages=messages,
                                     )
    return response['choices'][0]['message']['content']

def update_message(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

@st.cache_resource()
def database_conn():
    try: 
        conn = psycopg2.connect(**st.secrets["postgres"])
        return conn
    except Exception as e:
        print(e)
    


def run_query(conn, message, prompt_class):
    with conn.cursor() as cur:
        conn.rollback()
        cur.execute("INSERT INTO user_chat (messages, prompt_class) VALUES (%s, %s)",
                        (message, prompt_class))
        conn.commit()   
        
def date_time():
    date = datetime.now()
    formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date
