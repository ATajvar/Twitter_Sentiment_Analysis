# app.py
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analyzer", page_icon="🧠")
st.title("🧠 Real-Time Sentiment Analysis")

st.markdown("Enter a sentence below and I’ll tell you if it’s **Positive**, **Negative**, or **Neutral**.")

user_input = st.text_area("Your Text", height=150)

if st.button("Analyze Sentiment"):
    if user_input:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            result = "Positive 😊"
        elif polarity < -0.1:
            result = "Negative 😠"
        else:
            result = "Neutral 😐"

        st.subheader("Result:")
        st.write(result)
    else:
        st.warning("Please enter some text first.")