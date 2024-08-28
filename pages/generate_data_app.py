import streamlit as st
from openai import OpenAI


st.title("Data Generator")
# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = st.secrets["GPT_MODEL"]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    area_val = ("Trong vai trò là tư vấn viên chuyên tư vấn thông tin tuyển sinh của "
               "trường Đại học Ngoại ngữ - Tin học Thành phố Hồ Chí Minh (HUFLIT), hãy trả lời câu hỏi của người dùng."
               "Dưới đây là một số thông tin từ hệ thống:")

    instruction = st.text_area(
        "Các chỉ dẫn và ngữ cảnh kèm theo",
        value=area_val,
        height=300)

if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        instruction_msg = {
            "role": "system",
            "content": instruction,
        }
        history = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
        ]

        history.insert(0, instruction_msg)

        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=history,
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
