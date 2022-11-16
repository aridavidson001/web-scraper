import requests
import streamlit as st
from bs4 import BeautifulSoup


url = 'https://www.indeed.com/jobs?q=web+developer&l=New+York'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='results')
print(results)
st.write(results)
#print(results.prettify())
#st.write(results.prettify())
