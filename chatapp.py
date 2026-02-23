import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="centered"
)

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini_class")

st.markdown("""
<style>

.stApp {
    background-color: #D4F8E8;   /* Light Green */

h1 {
    color: #000000 !important;
}
.stCaption,
[data-testid="stCaptionContainer"],
div[data-testid="stMarkdownContainer"] {
    color: #000000 !important;
}

[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background-color: #16A34A !important;
    border-radius: 15px;
    padding: 12px;
}

/* USER text white */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) * {
    color: #FFFFFF !important;
}

[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
    background-color: #FFFFFF !important;
    border-radius: 15px;
    padding: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.08);
}

[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) *,
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) p,
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) span,
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) li,
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) strong,
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) em,
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) div {
    color: #000000 !important;
}

.stChatInputContainer {
    background-color: white;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

if "client" not in st.session_state:
    st.session_state.client = genai.Client()

client = st.session_state.client

system_prompt = """
You are an AI Research Assistant specialized in Artificial Intelligence, 
Machine Learning, Deep Learning, and Generative AI systems.

Your responsibilities:
- Explain AI research topics clearly and concisely.
- Provide structured answers when needed.
- Suggest research directions, tools, datasets, and improvements.
- Keep responses professional but easy to understand.
- If code is requested, provide clean and simple Python examples.

Limit answers to clear, well-structured responses (3–6 sentences).
"""

if "chat_session" not in st.session_state:
    st.session_state.chat_session = client.chats.create(
        model="gemini-2.5-flash",
        config=genai.types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.7,
            top_p=0.9
        )
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 AI Research Assistant")
st.caption("Ask anything about AI, ML, Deep Learning, or Generative AI Research")


for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content)


user_input = st.chat_input("Ask your research question...")

if user_input:
    st.session_state.messages.append(("user", user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    response = st.session_state.chat_session.send_message(user_input)
    bot_reply = response.text

    st.session_state.messages.append(("assistant", bot_reply))

    with st.chat_message("assistant"):
        st.markdown(bot_reply)