import streamlit as st
import requests
myApikey = "649e0292"

title = st.text_input("Type the title and press Enter")
if title:
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey={myApikey}"
        re = requests.get(url)
        re = re.json()
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(re["Poster"])
        with col2:
            st.subheader(re["Title"])
            st.caption(f"Genre: {re['Genre']} Year: {re['Year']}")
            st.write(re["Plot"])
            st.text(f"rating: {re['imdbRating']}")
            st.progress(float(re['imdbRating'])/10)
    except:
        st.error("No movie with that title")
