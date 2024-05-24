import streamlit as st

static_questions = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15']

with st.container():
    st.title("OpenAI Chatbot")
    st.write("This is a simple chatbot that uses OpenAI's GPT-3 model to generate responses to your messages.")
    st.write("Type a message in the chatbox below and the chatbot will respond to you.")
    for question in static_questions:
        st.write(question)