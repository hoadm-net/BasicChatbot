import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title('Fine-tuning ChatGPT')
st.header('Mục đích')
st.text("""
1. Tìm hiểu về Fine-tune LLMs, cụ thể là ChatGPT
2. Ứng dụng xây dựng Chatbot cơ bản trên fined-tune model.
3. Xây dựng quy trình tạo dữ liệu và đánh giá ứng dụng
""")

st.header('Ứng dụng')
st.text("""
1. Ứng dụng ChatGPT cơ bản
2. Ứng dụng ChatGPT để sinh dữ liệu
""")

st.sidebar.page_link("app.py", label="HomePage")
st.sidebar.page_link("pages/basic_app.py", label="GPT Chatbot")
st.sidebar.page_link("pages/generate_data_app.py", label="Generate Data")
