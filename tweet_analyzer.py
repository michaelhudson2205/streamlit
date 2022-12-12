
import streamlit as st
from textblob import TextBlob
import pyperclip

st.header('Tweet Count')

col1, col2 = st.columns([3,1])
with col1:
    text = st.text_area('Enter Tweet', max_chars=280)
with col2:
    st.write(' ')
    st.write(' ')
    copy = st.button('Copy Text')
    if copy:
        pyperclip.copy(text)
    st.write(' ')
    link = '[Post on Twitter](https://twitter.com/intent/tweet?text=&submit=Post+On+Twitter)'
    link
    st.markdown('<style>.css-1fv8s86 a {background-color:blue; color:white; padding:10px; border-radius:5px; text-decoration:none;}</style>', unsafe_allow_html=True)

blob = TextBlob(text)

col1, col2 = st.columns(2)
with col1:
    st.metric('Emotion', blob.sentiment.polarity)
with col2:
    st.metric('Subjectivity', blob.sentiment.subjectivity)
