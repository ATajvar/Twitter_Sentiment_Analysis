# 🧠 Real-Time Sentiment Analysis Web App

This is a minimalist web application that performs real-time sentiment analysis on user-inputted text using **TextBlob** and **Streamlit**.

It classifies input as **Positive**, **Negative**, or **Neutral**, based on sentiment polarity.

---

## 🚀 Live Demo

🔗 [Hosted on Streamlit Cloud](https://atajvar-sentiment-analysis.streamlit.app)

---

## 📦 Features

- Simple, single-page UI
- Real-time analysis with just type and click
- Clear output with emoji-based feedback
- Built using:
  - Python
  - [TextBlob](https://textblob.readthedocs.io/en/dev/)
  - [Streamlit](https://streamlit.io)

---

## 🧪 Example Inputs

| Input                               | Output     |
|-------------------------------------|------------|
| `What is the point of this anger?` | Negative 😠 |
| `What is the point of this happy?` | Positive 😊 |
| `What is the point of this melancholy?` | Neutral 😐 |

---

# 🛠️ Local Setup (Optional)


## Clone this repo
git clone https://github.com/ATajvar/Twitter_Sentiment_Analysis

cd Twitter_Sentiment_Analysis

## Install dependencies
pip install -r requirements.txt

## Run the app
streamlit run app.py

# Files
	•	app.py — Main Streamlit app
	•	requirements.txt — Project dependencies
    •	README.md - Readme and details