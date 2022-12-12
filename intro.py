import streamlit as st

title = st.title('News App')
st.header('Header')
st.subheader('subheader')
st.text('raw text')
st.caption('caption')
st.code('for i in range(20): print i')
st.markdown('# *heading1*')
st.write('<h1>This is normal writing by Mike</h1>', unsafe_allow_html=True)

btn = st.button('Click')
if btn:
    st.write("I was clicked")

with open('Mike_Selfie_220902.jpg', 'rb') as file:
    st.download_button(label='Download Image', data=file, file_name='Mike_Selfie_220902.jpg', mime='jpg')

ch = st.checkbox('I agree with the terms and conditions.')
if ch:
    st.write("Thanks for agreeing")

r = st.radio("Choose a category", ("business", "politics", "sports"))
if r:
    st.write("You chose ", r)

st.selectbox('Choose a category', ["business", "politics", "sports"])

st.multiselect('Choose a category', ["business", "politics", "sports"])

sl = st.slider("Choose a range", 0, 100)
st.write("you chose", sl)
st.select_slider('Choose ', ['jack', 'john', 'alex', 'mary', 'bob'])

col4, col5 = st.columns([1,3])
with col4:
    st.text_input("Your name her:")
with col5:
    st.text_area("Your message:")

st.number_input("Your age:")
st.time_input("Time here:")
st.date_input("Date")
st.color_picker("Colour")
st.file_uploader("Your file")



df = {'name':['jack', 'john', 'mary'], 'age':[25, 55, 30]}
st.dataframe(df)
st.table(df)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("temperature", "24 C", -4)
with col2:
    st.metric("temperature", "25 C", 1)
with col3:
    st.metric("temperature", "20 C", 8)

with st.expander("Click here"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("temperature", "24 C", -4)
    with col2:
        st.metric("temperature", "25 C", 1)
    with col3:
        st.metric("temperature", "20 C", 8)

with st.expander("Click here to see image"):
    st.image(
        "https://images.pexels.com/photos/208821/pexels-photo-208821.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")

    # sidebar
    st.sidebar.title("This is side bar")
    st.sidebar.button("sidebar button")

st.progress(75)

st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
e = RuntimeError("Something wrong")
st.exception(e)

import time
with st.spinner("Wait for 3 seconds..."):
    time.sleep(3)
st.write("thanks for waiting")

st.balloons()

# newsapi 42e460c6537f48c08ad3d69992c5b13a
