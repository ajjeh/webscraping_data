from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=USA').text

# print(html_text)
bsoup = BeautifulSoup(html_text, 'lxml')

job_card = bsoup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for jobs in job_card:
    # print(job_card)
    # job_title = job_card.find('strong', class_='blkclor')
    company_name = jobs.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    KeySkills = jobs.find('span', class_='srp-skills').text.replace(' ', '')
    publish_date = jobs.find('span', class_='sim-posted').span.text

    # print(job_title)
    # print(company_name)
    # print(KeySkills)


    print(f''' 
        Company Name: {company_name} 
        Required Skills: {KeySkills}''' )

    print('')