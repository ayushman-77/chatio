# 💬 Chatio — A Simple Streamlit Chatroom App

Chatio is a lightweight and persistent chatroom built with Python and Streamlit, where users can register with a username and password and participate in a shared public chatroom.

---

## 🚀 Features

- ✅ User Registration & Login
- ✅ Persistent Chat History (stored in `chat.json`)
- ✅ Styled Chat Interface with Timestamps
- ✅ Auto Refresh & Manual Refresh Support
- ✅ Local JSON-based User Authentication (`users.json`)

---

## 📦 Requirements

- Python 3.7+
- Streamlit

Install dependencies:

```bash
pip install streamlit
```

---

## 📁 Project Structure

```
chatio/
├── app.py           # Main Streamlit chatroom app
├── chat_data.json   # Stores persistent chat messages
├── users.json       # Stores hashed user credentials
└── README.md        # Project documentation
```

---

## ▶️ How to Run

```bash
streamlit run app.py
```

---

## 🧪 Demo

- Register with a new username and password
- Start chatting immediately
- Refresh the chat manually or let it auto-refresh when you send messages

---

## 🔐 Note

- This app uses simple SHA256 hashing for passwords. For real production apps, switch to more secure methods (e.g., bcrypt, OAuth).
- This is intended for **local/demo usage**. Do not expose it directly to the internet without adding proper security.