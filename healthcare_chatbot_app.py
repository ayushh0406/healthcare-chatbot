import streamlit as st
from healthcare_chatbot import rule_based_response, get_greeting_response

def render_chat(sender, message):
    if sender == "You":
        st.markdown(
            f"<div style='text-align: right;'>"
            f"<span style='display:inline-block; background:#CFE2FF; color:#2085d9; padding:10px 15px; border-radius:20px 20px 6px 20px; margin:6px 0;'><b>🧑‍💻</b> {message}</span>"
            f"</div>", unsafe_allow_html=True)
    else:
        st.markdown(
            f"<div style='text-align: left;'>"
            f"<span style='display:inline-block; background:#FFF7E6; color: #CA893E; padding:10px 15px; border-radius:20px 20px 20px 6px; margin:6px 0;'><b>🤖</b> {message}</span>"
            f"</div>", unsafe_allow_html=True)

st.set_page_config(page_title="Healthcare Chatbot", page_icon="🩺", layout="centered")
# Set a subtle background with CSS for visual appeal
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(120deg, #f1f7fc 0%, #ffe6e6 100%);
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<h1 style='text-align:center;color:#2085d9;'>🩺 Healthcare Chatbot</h1>"
    "<div style='text-align:center;'><img src='https://img.icons8.com/clouds/100/000000/clinic.png'/></div>"
    "<p style='text-align:center; font-size: 1.05rem; color:#444;'>How can I help you today?</p>",
    unsafe_allow_html=True
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def on_submit():
    user_text = st.session_state.user_input
    if user_text:
        response = rule_based_response(user_text)
        st.session_state.chat_history.append(("You", user_text))
        st.session_state.chat_history.append(("Bot", response))
        st.session_state.user_input = ""

st.text_input(
    "You:",
    key="user_input",
    on_change=on_submit,
    placeholder="Type your health question here..."
)

# Don't put chat messages in a fixed-height box—show as a flowing feed
if not st.session_state.chat_history:
    st.markdown(
        "<div style='text-align:center;'><span style='font-size:2rem;'>👋</span><br>"
        "<span style='color:#bbb;'>Type something to start the conversation!</span></div>",
        unsafe_allow_html=True,
    )
else:
    for sender, msg in st.session_state.chat_history:
        render_chat(sender, msg)

st.markdown(
    "<p style='text-align:center;font-style:italic;color:#aaa;'>"
    "Type 'exit', 'quit', or 'bye' to end the chat · Stay healthy!"
    "</p>",
    unsafe_allow_html=True
)
