import streamlit as st
import requests

apiKey = 'JTQn6fNKDyyAHJqrCBBiVu6ngbh6b9bvZNNWjzQz'

st.markdown('<iframe src="https://embed.lottiefiles.com/animation/24118"></iframe>', unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)
with col1:
    curr1 = st.selectbox('Currency 1', ('AUD', 'JPY', 'USD'))
with col2:
    if curr1 == 'AUD':
        # st.markdown('<iframe src="https://embed.lottiefiles.com/animation/24848"></iframe>', unsafe_allow_html=True)
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/89032"></iframe>', unsafe_allow_html=True)
    elif curr1 == 'JPY':
        # st.markdown('<iframe src="https://embed.lottiefiles.com/animation/24844"></iframe>', unsafe_allow_html=True)
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/89033"></iframe>', unsafe_allow_html=True)
    else:
        # st.markdown('<iframe src="https://embed.lottiefiles.com/animation/24845"></iframe>', unsafe_allow_html=True)
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/88338"></iframe>', unsafe_allow_html=True)
with col3:
    curr2 = st.selectbox('Currency 2', ('JPY', 'USD', 'AUD'))

# url = f'https://free.currconv.com/api/v7/convert?q={curr1}_{curr2},{curr2}_{curr1}&compact=ultra&apiKey={apiKey}'
url = f'https://api.freecurrencyapi.com/v1/latest?base_currency={curr1}&currencies={curr2}&apikey={apiKey}'

re = requests.get(url)
re = re.json()
# one_two = re[f"{curr1}_{curr2}"]
# two_one = re[f"{curr2}_{curr1}"]
c_one = re['data'][f'{curr2}']
c_two = 1 / c_one

col1, col2 = st.columns(2)
with col1:
    st.write(f"One {curr1} is worth this much {curr2}:")
    # st.success(one_two)
    st.success(c_one)
with col2:
    st.write(f"One {curr2} is worth this much {curr1}:")
    # st.success(two_one)
    st.success(c_two)

col1, col2 = st.columns(2)
with col1:
    amount = st.number_input(f"Input the amount of {curr1} you wish to convert:")
with col2:
    # converted = amount * one_two
    converted = amount * c_one
    st.text(f"Converted amount of {curr1} to {curr2}:")
    st.success(converted)

st.markdown('<style>body{text-align:center;} #MainMenu, footer{visibility:hidden;} .css-ffhzg2{background-color:#001253}</style>', unsafe_allow_html=True)
