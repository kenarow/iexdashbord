import streamlit as st
import requests
import symtable

from iex import IEXStock
r = requests.get('https://www.python.org')
import config

symbol = st.sidebar.text_input("Symbol", value="AAPL") 

stock = IEXStock(config.IEX_API_TOKEN, symbol) 

screen = st.sidebar.selectbox("View", ('Overview', 'Fondamentals', 'News', 'Ownership', 'Technicals'))

st.title(screen)

if screen == 'Overview':
    logo = stock.get_logo()
    company_info = stock.get_company_info()

    col1, col2 = st.columns([1, 4]) 
    
    with col1:
        st.image(logo['url'])

    with col2:
        st.subheader(company_info['companyName'])
        st.subheader('Description')
        st.write(company_info['description'])
        st.subheader('Industry')
        st.write(company_info['industry'])
        st.subheader('CEO')
        st.write(company_info['CEO'])

if screen == 'Fondamentals':
    stats = stock.get_stats()
    st.write(stats)
