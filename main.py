import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1,1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("counting your money...")
    time.sleep(1)
    amount=generate_money()
    st.success(f"You made {amount} rupees!")

def fetch_side_hustles():
    try:
        response=requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles=response.json()
            return hustles["side_hustle"]
        else:
            return ("Check your internet connection")
    except:
        return ("Something Went Wrong!")
    
st.subheader("Side Hustle Ideas")
if st.button("Generate a side hustle"):
    idea=fetch_side_hustles()
    if (idea =="Something Went Wrong!" or idea == "Check your internet connection" ):
        st.error(idea)
    else:
        st.success(idea)

def fetch_money_quotes():
    try:
        response=requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes=response.json()
            return quotes["money_quotes"]
        else:
            return ("Check your internet connection")
    except:
        return ("Something Went Wrong!")
    
st.subheader("Money Quotes")
if st.button("Generate a Money Quote"):
    quote=fetch_money_quotes()
    if (quote =="Something Went Wrong!" or quote == "Check your internet connection" ):
        st.error(quote)
    else:
        st.success(quote)