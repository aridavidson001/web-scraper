import csv
import requests
from bs4 import BeautifulSoup
import streamlit as st

url = 'https://www.indeed.com/jobs?q=web+developer&l=New+York'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#results = soup.find(id='resultsCol')
print(soup.prettify())
st.write(soup.prettify())

'''
url = 'https://www.indeed.com/jobs?q=web+developer&l=New+York'
page = requests.get(url)
st.write(page.content)
st.write(page.status_code)
'''



'''url = 'http://api.scraperapi.com?api_key=f894cc3b0ca8e6b70619aa940b31139a&url=https://www.indeed.com/jobs?q=web+developer&l=New+York'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsCol')
indeed_jobs = results.select('div.jobsearch-SerpJobCard.unifiedRow.row.result')
file = open('indeed-jobs.csv', 'w')
writer = csv.writer(file)
# write header rows
writer.writerow(['Title', 'Company', 'Location', 'Apply'])
for indeed_job in indeed_jobs:
   job_title = indeed_job.find('h2', class_='title').text.strip()
   job_company = indeed_job.find('span', class_='company').text.strip()
   job_location = indeed_job.find('span', class_='location accessible-contrast-color-location').text.strip()
   job_url = indeed_job.find('a')['href']
   writer.writerow([job_title.encode('utf-8'), job_company.encode('utf-8'), job_location.encode('utf-8'), job_url.encode('utf-8')])
file.close()
'''
