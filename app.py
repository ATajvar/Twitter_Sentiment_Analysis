# app.py
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Real-Time Sentiment Analysis", page_icon="🧠")

# Page Title
st.title("🧠 Real-Time Sentiment Analysis")
st.markdown("Enter a sentence below and I’ll tell you if it’s **Positive**, **Negative**, or **Neutral.**")

# Input box
with st.container():
    user_input = st.text_area("Your Text", height=150)

# Analyze button
if st.button("Analyze Sentiment"):
    if user_input:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        # Basic threshold logic
        if polarity > 0.1:
            sentiment = "Positive 😊"
        elif polarity < -0.1:
            sentiment = "Negative 😠"
        else:
            sentiment = "Neutral 😐"

        st.subheader("Result:")
        st.markdown(f"**{sentiment}**")
        st.caption(f"Polarity Score: {polarity:.2f}")
    else:
        st.warning("Please enter some text first.")