# Import necessary libraries
import streamlit as st
import requests

# Function to send login data to a backend
def send_to_backend(username, password):
    host = "http://0.0.0.0:8000"
    login_url = f"{host}/login"
    
    data = {
        'username': username,
        'password': password
    }

    response = requests.post(login_url, json=data)
    return response.json()

# Streamlit App
st.title("Login Page")

with st.form("login_form"):
    st.write("Please enter your login details")
    
    username = st.text_input("Username", type="default")
    password = st.text_input("Password", type="password")

    submit_button = st.form_submit_button("Login")
    
    if submit_button:
        response = send_to_backend(username, password)
        if response.get('status') == "success":
            st.success("Login successful!")
        else:
            st.error("Login failed!")

# Add some minimalistic styling
st.markdown("""
    <style>
        body {
            color: #2c3e50;
            background-color: #ecf0f1;
        }
        .stButton>button {
            background-color: #2980b9;
            color: #ecf0f1;
        }
    </style>
""", unsafe_allow_html=True)
