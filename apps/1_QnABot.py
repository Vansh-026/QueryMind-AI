from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

st.title("QueryMind AI: Your Personal AI Assistant")
st.markdown("Welcome to QueryMind AI! Ask me anything, and I'll do my best to assist you.")

if "messages" not in st.session_state:
    st.session_state.messages=[]
    
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask Anything ?")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    response = llm.invoke(query)
    st.chat_message("AI").markdown(response.text)
    st.session_state.messages.append({"role": "AI", "content": response.text})