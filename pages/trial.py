import streamlit as st
import streamlit.components.v1 as com
from streamlit_chat import message
from bokeh.models import CustomJS
from streamlit_extras.colored_header import colored_header
from bokeh.models.widgets import Button
from streamlit_bokeh_events import streamlit_bokeh_events
import openai
from streamlit_extras.switch_page_button import switch_page
from dotenv import load_dotenv, find_dotenv
import datetime
import os
import sys
sys.path.append("..")
from util import initial_message, get_response, update_message, database_conn, run_query, date_time


load_dotenv(find_dotenv())

st.set_page_config(page_title="Streamlit Web App", initial_sidebar_state="collapsed", layout="wide")
st.title("Lets talk ")

con = database_conn()



if 'past' not in st.session_state:
    st.session_state['past'] = ["Here you goooo"]
    
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hi and welcome here "]




response_container = st.container()
input_container = st.container()




#User input
# Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text
    

user_input = get_text()


if "messages" not in st.session_state:
    st.session_state["messages"] = initial_message()
    
# # ## Applying the user input box
with input_container:  
    if user_input:
        date = date_time()
        run_query(conn=con, message=user_input, prompt_class='Prompt_1')
        messages = st.session_state['messages']
        messages = update_message(messages=messages, role="user", content=user_input)
        response = get_response(messages=messages)
        messages = update_message(messages=messages, role="assistant", content=response)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)



with response_container:     
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))


end_conversation = st.button("End Conversation")

if end_conversation:
    switch_page("main")
    #create a summary of all that has been said
    