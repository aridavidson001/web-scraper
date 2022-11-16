import csv
import requests
from bs4 import BeautifulSoup
import streamlit as st

url = 'http://api.scraperapi.com?api_key=f894cc3b0ca8e6b70619aa940b31139a&url=https://www.indeed.com/jobs?q=web+developer&l=New+York'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print (soup.find(id='resultsCol'))
results = (soup.find(id='resultsCol')
indeedjobs = results.select('div.jobsearch-SerpJobCard.unifiedRow.row.result')
file = open('indeed-jobs.csv', 'w')
writer = csv.writer(file)
# write header rows
writer.writerow(['Title', 'Company', 'Location', 'Apply'])
for indeedjob in indeed_obs:
   job_title = indeedjob.find('h2', class_='title').text.strip()
   job_company = indeedjob.find('span', class_='company').text.strip()
   job_location = indeedjob.find('span', class_='location accessible-contrast-color-location').text.strip()
   job_url = indeedjob.find('a')['href']
   writer.writerow([job_title.encode('utf-8'), job_company.encode('utf-8'), job_location.encode('utf-8'), job_url.encode('utf-8')])
file.close()

