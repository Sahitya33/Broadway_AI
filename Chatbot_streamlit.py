import streamlit as st
import os
from dotenv import load_dotenv
import re
from groq import Groq

st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Chatbot")

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=GROQ_API_KEY)

system_prompt = "You are a helpful assistant. Remember what the user says and use that information in later answers."
system_message = {"role": "system", "content": system_prompt}

if "conversation" not in st.session_state:
    st.session_state.conversation = [system_message]

for msg in st.session_state.conversation:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**Assistant:** {msg['content']}")

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask anything:")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip() != "":

    user_message = {"role": "user", "content": user_input}
    st.session_state.conversation.append(user_message)

    response = groq_client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=st.session_state.conversation,
        max_tokens=2000,
        temperature=0.7
    )

    assistant_message = response.choices[0].message.content
    assistant_message = re.sub(r"<think>.*?</think>", "", assistant_message, flags=re.DOTALL).strip()
    st.session_state.conversation.append({"role": "assistant", "content": assistant_message})

    st.rerun()

if st.button("🗑️ Clear Chat"):
    st.session_state.conversation = [system_message]
    st.rerun()