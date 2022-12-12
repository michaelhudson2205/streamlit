

import streamlit as st
import requests
import pycountry
apiKEY = "42e460c6537f48c08ad3d69992c5b13a"

st.title("News App")

col1, col2 = st.columns([3,1])
with col1:
    user = st.text_input("Enter Country Name")
with col2:
    category = st.radio("Choose a news category", ("Technology", "General", "Sports", "Business"))
    btn = st.button("Enter")

if btn:
    country = pycountry.countries.get(name=user).alpha_2
    cat = category.lower()
    if cat == "general":
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={apiKEY}"
    else:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&q={cat}&apiKey={apiKEY}"
    r = requests.get(url)
    r = r.json()
    articles = r["articles"]
    for article in articles:
        st.header(article["title"])
        st.write("Published at: ", article["publishedAt"])
        if article["author"]:
            st.write("Author: ", article["author"])
        st.write("Source", article["source"]["name"])
        st.write("Description: ", article["description"])
        if article["urlToImage"]:
            st.image(article["urlToImage"])
