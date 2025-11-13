import streamlit as st
import json
import os
import subprocess
import time

# ==================== CONFIG ====================
st.set_page_config(page_title="KrushiSetu Login", page_icon="🌿", layout="wide")

# ==================== DATABASE FILE ====================
USER_FILE = "users.json"
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)



# ==================== CUSTOM STYLE ====================
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #d9f7d9, #f1fff1);
    font-family: 'Poppins', sans-serif;
}
.login-box {
    background: white;
    width: 420px;
    margin: 100px auto;
    padding: 40px 50px;
    border-radius: 20px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.1);
}
h1 {
    text-align: center;
    color: #2e8b57;
    margin-bottom: 25px;
}
button {
    background-color: #2e8b57;
    color: white;
    font-size: 18px;
    font-weight: 600;
    padding: 10px 20px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
}
button:hover {
    background-color: #45a049;
}
.footer {
    text-align: center;
    color: #2e8b57;
    margin-top: 30px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ==================== APP TITLE ====================
st.markdown("<h1>🌿 KrushiSetu</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#2e8b57;font-size:18px;'>Empowering Farmers with AI-Powered Crop Health Insights</p>", unsafe_allow_html=True)

# ==================== LOGIN / SIGNUP TABS ====================
tab_login, tab_signup = st.tabs(["🔑 Login", "🆕 Sign Up"])
users = load_users()

# =============== LOGIN PAGE ===============
with tab_login:
    with st.form("login_form"):
        email = st.text_input("📧 Email Address")
        password = st.text_input("🔒 Password", type="password")
        login_btn = st.form_submit_button("Login ✅")

        if login_btn:
            if email in users and users[email]["password"] == password:
                st.success("Login successful 🌿 Redirecting...")
                time.sleep(1)
                subprocess.Popen(["streamlit", "run", "krushi_ui.py"], shell=True)
                st.stop()
            else:
                st.error("Invalid credentials ❌")

# =============== SIGN UP PAGE ===============
with tab_signup:
    with st.form("signup_form"):
        name = st.text_input("👤 Full Name")
        email_s = st.text_input("📧 Email Address")
        password_s = st.text_input("🔒 Password", type="password")
        signup_btn = st.form_submit_button("Create Account 🌾")

        if signup_btn:
            if email_s in users:
                st.warning("Account already exists ⚠️")
            elif not name or not email_s or not password_s:
                st.error("Please fill all fields ❗")
            else:
                users[email_s] = {
                    "name": name,
                    "email": email_s,
                    "password": password_s
                }
                save_users(users)
                st.success("Account created successfully 🌿 Redirecting...")
                time.sleep(1)
                subprocess.Popen(["streamlit", "run", "krushi_ui.py"], shell=True)
                st.stop()

st.markdown("<p class='footer'>©2025 KrushiSetu | Developed by Team GreenMind 🌱</p>", unsafe_allow_html=True)