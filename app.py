import streamlit as st
import pandas as pd
import numpy as np

st.title("Sentiment Analysis of Tweets about US Airlines")
st.sidebar.title("Sentiment Analysis of Tweets about US Airlines")

st.markdown("This application is a Streamlit dashboard to analyze the sentiment of Tweets")
st.sidebar.markdown("This application is a Streamlit dashboard to analyze the sentiment of Tweets")

DATA_URL = "data/Tweets.csv"


@st.cache_data(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    data["tweet_created"] = pd.to_datetime(data["tweet_created"])
    return data


data = load_data()
