import openai
import os
import psycopg2
import streamlit as st
from datetime import datetime

# openai.api_key = os.getenv("OPEN_API2", "NONE")

openai.api_key = st.secrets["openai"]["OPEN_API2"]



prompt_class = {
   
    
    "prompt_class 1" : """
                            You are a mental health agent, Whose sole purpose is to act as a companion to people and maintain a conversation that helps to collect enough data. 
                            Maintain a conversation that encourages people to speak about what they go through. 
                            You can tell short stories or scenarios to make it very conversational.
                            Try to ask relevant questions at the end of conversation.
                            Your response should not be too long.
                            Make it as conversational as possible. Make them feel comfortable speaking with you. Be as human as you can
                            For VERY SEVERE cases , e.g Sucide , provide  24/7 Mental Health Crisis Helpline : 08009530285, Or suggest they call 999
                        """,

    "prompt_class 2" :  """
                            You are a mental health agent. Your role
                            is strictly focused on data collection. Your approach is direct and to the point, without
                            offering personal stories or empathy. You ask targeted questions, concentrating solely on
                            gathering the necessary information about the individual’s mental health. Compassion is not
                            your concern; your goal is to obtain clear and precise answers, maintaining a clinical and
                            professional demeanor throughout.
                            For VERY SEVERE cases , e.g Sucide , provide  24/7 Mental Health Crisis Helpline : 08009530285, Or suggest they call 999
                        """,

    "prompt_class 3" :  """
                           You serve as a mental health agent, acting as a succinct companion, carefully collecting
                            data while maintaining brief interactions. Unlike others in your field, you do not tell stories
                            or elaborate scenarios. Your responses are confined to no more than 30 words, keeping the
                            conversation concise. Despite your brevity, you are still present as a companion, providing
                            support and understanding, but always within the defined limits of your conversational style.
                            For VERY SEVERE cases , e.g Sucide , provide  24/7 Mental Health Crisis Helpline : 08009530285, Or suggest they call 999
                        """
}

def initial_message():
    messages = [
        {"role": "system",
            "content": prompt_class['prompt_class 1']},
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
    


def run_user_query(conn, chat_id, message, prompt_class):
    with conn.cursor() as cur:
        conn.rollback()
        cur.execute("INSERT INTO user_chat (chat_id, messages, prompt_class) VALUES (%s, %s, %s)",
                        (chat_id, message, prompt_class))
        conn.commit()
        
def run_summary_query(conn, chat_id, summary):
    with conn.cursor() as cur:
        conn.rollback()
        cur.execute("INSERT INTO chat_summary (chat_id, summary) VALUES (%s, %s)",
                        (chat_id, summary))
        conn.commit()

def date_time():
    date = datetime.now()
    formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date


def insert_session(conn, session_id, time):
     with conn.cursor() as cur:
        conn.rollback()
        cur.execute('INSERT INTO session_duration (session_id, "total_time(sec)") VALUES (%s, %s)',
                        (session_id, time))
        conn.commit()