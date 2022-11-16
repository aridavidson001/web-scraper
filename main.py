import requests
import streamlit as st
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsCol')
st.write(results.prettify())
