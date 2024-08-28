# Basic Chatbot

Công cụ đơn giản hỗ trợ việc tìm hiểu và xây dựng ứng dụng Chatbot dựa trên LLMs

## 1. Cài đặt

Để sử dụng, trước hết cần cài đặt
1. Môi trường ảo Python
2. Cài đặt các gói cơ bản:
	* [streamlit](https://docs.streamlit.io/get-started/installation)
	* [openai](https://platform.openai.com/docs/libraries)
3. Tạo folder .streamlit
4. Tạo 2 files cấu hình trong folder vừa tạo ở bước 3

```
# config.toml

[client]
showSidebarNavigation = false
```

```
# secrets.toml

OPENAI_API_KEY="sk-......"
GPT_MODEL="gpt-4o"
```

## 2. Sử dụng

1. Kích hoạt môi trường ảo
2. Thực thi lệnh
```streamlit run app.py```