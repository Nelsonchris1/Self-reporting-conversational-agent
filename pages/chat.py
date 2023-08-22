import streamlit as st
import streamlit.components.v1 as com
from streamlit_chat import message
import openai
from streamlit_extras.switch_page_button import switch_page
import sys
sys.path.append("..")
from util import initial_message, get_response, update_message, database_conn, run_summary_query, run_user_query, date_time, insert_session
import shortuuid
import webbrowser
import time



st.set_page_config(page_title="Streamlit Web App", initial_sidebar_state="collapsed", layout="wide")
st.title("Lets talk ")

con = database_conn()

if 'start_time' not in st.session_state:
    st.session_state['start_time'] = time.time()

start_time = st.session_state['start_time']


if 'past' not in st.session_state:
    st.session_state['past'] = [" "]
    
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hi and welcome here "]




response_container = st.container()
input_container = st.container()


if "something" not in st.session_state:
    st.session_state.something = ''


def submit():
    st.session_state.something = st.session_state.widget
    st.session_state.widget = ''


#User input
# Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="widget", on_change=submit)
    return st.session_state.something
    


user_input = get_text()
post_prompt = "INSTRUCTION, Do not answer question not related to the context of Mental health. "

if "messages" not in st.session_state:
    st.session_state["messages"] = initial_message()

if "session_id" not in st.session_state:
    st.session_state.session_id = shortuuid.uuid()
    
# # ## Applying the user input box
with input_container:  
    if user_input:
        date = date_time()
        run_user_query(conn=con, chat_id = st.session_state.session_id, message=user_input, prompt_class="prompt_class 1")
        messages = st.session_state['messages']
        messages = update_message(messages=messages, role="user", content=user_input + ". " + post_prompt)
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

prompt_link_1 = "https://docs.google.com/forms/d/e/1FAIpQLSejKgCKHPp2Bnt1pgbXh4KZZT8gA3T1WTHIql0n32ROF2Pe7w/viewform"
prompt_link_2 = "https://docs.google.com/forms/d/e/1FAIpQLScnVXtutqGwzmRGYcdnCn1vYFSdmxtKHo4OMjVDbfBGt3qR6g/viewform"
prompt_link_3 = "https://docs.google.com/forms/d/e/1FAIpQLSd73ALkRdvQ29aMWwgDS3Iq_kCiU81MKBmYnYbfYQd8FG8How/viewform"


if end_conversation:
    session_duration = time.time() - start_time
    insert_session(conn=con, session_id = st.session_state.session_id, time=session_duration)

    messages = update_message(messages=messages, role="user", content="Give me a summary of the chat")
    response = get_response(messages=messages)
    try:
        run_summary_query(conn=con, chat_id = st.session_state.session_id,
                        summary=response)
    
    except Exception as e:
        print(e)
    st.write('<meta http-equiv="refresh" content="0;url=' + prompt_link_1 + '">', unsafe_allow_html=True)
    switch_page("main")

   