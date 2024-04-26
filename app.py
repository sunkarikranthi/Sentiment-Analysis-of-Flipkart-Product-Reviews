import streamlit as st
from joblib import load

st.title('Welcome to Sentiment Analysis')
user_review = st.text_input('Enter your review')

# Load the model
model = load('best_models/best_model.pkl')


if st.button("Find Sentiment"):
    prediction = model.predict([str(user_review)])
    st.write(prediction[0])