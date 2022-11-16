import requests
import streamlit as st
url = 'https://www.indeed.com/jobs?'
page = requests.get(url)
st.write(page.content)
