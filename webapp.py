# importing libraries

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import numpy as np
import re
import string
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer, WordNetLemmatizer
from functions import *
import pickle
import logging
import os

# ---------------------------
# Setup Logging
# ---------------------------
log_file = os.getenv("LOG_FILE_PATH", "/var/log/app/webapp.log")
os.makedirs(os.path.dirname(log_file), exist_ok=True)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

if logger.hasHandlers():
    logger.handlers.clear()

file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
logger.addHandler(console_handler)

# ---------------------------
# Streamlit UI
# ---------------------------

# Page title and logo
image = Image.open('images/logo.png')
st.image(image, use_column_width=True)

st.write('''
# Cyberbulling Tweet Recognition App

This app predicts the nature of the tweet into 6 Categories.
* Age
* Ethnicity
* Gender
* Religion
* Other Cyberbullying
* Not Cyberbullying

***
''')

# Text Box
st.header('Enter Tweet ')
tweet_input = st.text_area("Tweet Input", height=150)
st.write('***')

# Display entered text
st.header("Entered Tweet text")
if tweet_input:
    st.write(tweet_input)
else:
    st.write('***No Tweet Text Entered!***')
st.write('***')

# Prediction Output
st.header("Prediction")
if tweet_input:
    prediction = custom_input_prediction(tweet_input)
    logging.info(f"Prediction: {prediction} for input: {tweet_input}")

    if prediction == "Age":
        st.image("images/age_cyberbullying.png", use_column_width=True)
    elif prediction == "Ethnicity":
        st.image("images/ethnicity_cyberbullying.png", use_column_width=True)
    elif prediction == "Gender":
        st.image("images/gender_cyberbullying.png", use_column_width=True)
    elif prediction == "Not Cyberbullying":
        st.image("images/not_cyberbullying.png", use_column_width=True)
    elif prediction == "Other Cyberbullying":
        st.image("images/other_cyberbullying.png", use_column_width=True)
    elif prediction == "Religion":
        st.image("images/religion_cyberbullying.png", use_column_width=True)
else:
    st.write('***No Tweet Text Entered!***')

st.write('***')

# About section
expand_bar = st.expander("About")
expand_bar.markdown('''
* **Source Code:** [https://github.com/apurvayadav/cyberbullying-tweet-recognition-app](https://github.com/apurvayadav/cyberbullying-tweet-recognition-app)
* **Dataset:** [https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification)
''')
