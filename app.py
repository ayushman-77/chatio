import streamlit as st
import json
import os
from datetime import datetime
import hashlib

CHAT_FILE = "chat_data.json"
USERS_FILE = "users.json"

def load_chat():
    if not os.path.exists(CHAT_FILE):
        return []
    with open(CHAT_FILE, "r") as f:
        return json.load(f)

def save_chat(log):
    with open(CHAT_FILE, "w") as f:
        json.dump(log, f, indent=2)

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, "r") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            else:
                return {}
    except json.JSONDecodeError:
        return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(username, password):
    users = load_users()
    return username in users and users[username] == hash_password(password)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = hash_password(password)
    save_users(users)
    return True

def post_message(user, msg):
    log = load_chat()
    log.append({
        "user": user,
        "msg": msg,
        "time": datetime.utcnow().isoformat()
    })
    save_chat(log)

st.set_page_config("ChatIO Room", layout="centered")

if "username" not in st.session_state:
    st.title("🔐 ChatIO Login")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        login_user = st.text_input("Username", key="login_user")
        login_pass = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            if authenticate_user(login_user, login_pass):
                st.session_state.username = login_user
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials.")

    with tab2:
        reg_user = st.text_input("New Username", key="reg_user")
        reg_pass = st.text_input("New Password", type="password", key="reg_pass")
        if st.button("Register"):
            if register_user(reg_user, reg_pass):
                st.success("✅ Registered! You can log in now.")
            else:
                st.warning("⚠️ Username already exists.")
    st.stop()

st.title("💬 ChatIO Public Room")
st.write(f"👋 Welcome, **{st.session_state.username}**")

msg = st.text_input("Type your message", key="msg_input")
if st.button("Send") and msg.strip():
    post_message(st.session_state.username, msg.strip())
    st.rerun()

st.subheader("📜 Chat History")

chat = load_chat()
for item in reversed(chat[-100:]):
    time_str = datetime.fromisoformat(item['time']).strftime("%H:%M:%S")
    user = item['user']
    message = item['msg']
    if user == st.session_state.username:
        st.markdown(f"<div style='color:black; background-color:#e6f2ff; padding:8px; border-radius:6px; margin-bottom:4px;'><b>You</b> [{time_str}]: {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='color:black; background-color:#f0f0f0; padding:8px; border-radius:6px; margin-bottom:4px;'><b>{user}</b> [{time_str}]: {message}</div>", unsafe_allow_html=True)

st.markdown("---")
if st.button("🔄 Refresh Chat"):
    st.rerun()

if st.button("🚪 Logout"):
    del st.session_state.username
    st.rerun()