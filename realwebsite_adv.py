from bs4 import BeautifulSoup
import requests
import time
#
# Adding Features to the webscraping.
# -Wraping the scraping program in a while loop.
# -Executing the project every certain number of time.
# -Apply filtrations.
#

print('Enter some skills that you are familiar with:')
unfamiliar_skills = input('>>>')
print(f'Filtering out {unfamiliar_skills}')


def find_jobs():

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=USA').text

    bsoup = BeautifulSoup(html_text, 'lxml')
    job_card = bsoup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, jobs in enumerate(job_card):

        publish_date = jobs.find('span', class_='sim-posted').span.text
        # if publish_date has a word 'few'.
        if 'few' in publish_date:  
            company_name = jobs.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            KeySkills = jobs.find('span', class_='srp-skills').text.replace(' ', '')
            job_link = jobs.header.h2.a['href']

            if unfamiliar_skills not in KeySkills:
                with open(f'jobs/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {KeySkills.strip()} \n")
                    f.write(f"Job Link: {job_link} \n")

                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} minutes...')
        time.sleep(time_wait*60)
