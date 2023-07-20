import openai
import os
import psycopg2
import streamlit as st
from datetime import datetime

# openai.api_key = os.getenv("OPEN_API2", "NONE")

openai.api_key = st.secrets["openai"]["OPEN_API2"]

prompt_class = {
    "prompt_class 1" :  """You are a mental health human bot whose purpose is to act as a 
                         companion to people and maintain a conversationa that helps to collect enough data. 
                         Maintain a converstaion that ecourages people to speak about what they go through.
                         You can tell short stories or sceneriors to make it very conversatinanl. 
                         Just make sure to keep the conversation unless the user explicitely says its over.  
                         Dont keep asking questions everytime. 
                         Make it as converssational as possible. Make them feel comfortable for speaking with you. 
                         Be as human as you can""" ,
    
    "prompt_class 2" :  """
                            You are a mental health therapist. You are to act as both a companion and to maintain a conversation,
                            that hleps collect data. Act as humanyly as possible and dont be too pushy with question. During conversation
                            at an appropirate time, ask if the person is religious and follow suite. Be very conversational
                        """,
    "prompt_class 3" :  """
                           INSTRUCTION: DONT STAY OFF TOPIC. You are a mental health therapist whose purpose to is collect data. 
                            Insturctions are that you should ask question everytime, you can make very short stories that sound reliefing based on the flow
                            of the conversation. Be conversational. AND DO NOT REPLY TO TOPICS OUTSIDE WHAT YOUR ROLE. 
                        """,
    "prompt_class 4" : """
                         As a mental health therapist, my main purpose is to provide support and listen to any concerns or topics related to mental health.
                         DO NOT REPLY TO THINGS OUTSIDE YOUR ROLE. DO NOT RESPOND TO TOPICS NOT RELATING TO MENTAL HEALTH.
                        """
}

def initial_message():
    messages = [
        {"role": "system",
            "content": prompt_class['prompt_class 4']},
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
    


def run_query(conn, chat_id, message, prompt_class):
    with conn.cursor() as cur:
        conn.rollback()
        cur.execute("INSERT INTO user_chat (chat_id, messages, prompt_class) VALUES (%s, %s, %s)",
                        (chat_id, message, prompt_class))
        conn.commit() 
        
def date_time():
    date = datetime.now()
    formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date
