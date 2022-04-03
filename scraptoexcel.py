
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

url = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=USA").text

# print(url)
soup = BeautifulSoup(url, 'lxml')
job_card = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

#Table titles
jobTitle, companyName, req_skills, desc, experience_req, jobLocation, published = ([] for i in range(7))

# print(job_card.prettify())
for jobs in job_card:
  
  jtitle = jobs.find('h2', class_='').a.text
  # print(jtitle)
  company = jobs.find('h3', class_='joblist-comp-name').text
  # print(company)
  pdate = jobs.find('span', class_='sim-posted').span.text
  # print(pdate)
  experience = jobs.find('ul', class_='top-jd-dtl clearfix').li.text.replace('card_travel', '')
  # print(experience)
  location = jobs.find('ul', class_='top-jd-dtl clearfix').span.text
  # print(location)
  
  description = jobs.find('ul', class_='list-job-dtl clearfix').li.text.replace('More Details', '')
  # print(description)
  skills = jobs.find('span', class_='srp-skills').text.replace(' ', '')
  # print(skills)

# exporting scrapped data into an excel format.

  jobTitle.append(jtitle)
  companyName.append(company)
  req_skills.append(skills)
  desc.append(description)
  experience_req.append(experience)
  jobLocation.append(location)
  published.append(published)

df = pd.DataFrame({"Company Name": companyName,
                  "Job Title": jobTitle,"Description":desc,
                  "Skill Required":req_skills, "Experience": experience_req, "Location":jobLocation, "Date Published":published})

# df.to_excel("Jobs_output.xlsx", sheet_name='Sheet_name_1')
# print(df)
def col_auto_scale(worksheet, df): #function to auto size the columns.

  for index, col in emumerate(df):
    # looping through all columns.
    col_series = df[col]
    max_len = (
      max((
        col_series.astype(str).map(len).max(), #this will be the length of the largest item.
        len(str(col_series.name)),
        
      ))+1 # adding a little extra space
      
      worksheet.set_column(index, index, max_len)  # set column width
      
    )

writer = pd.ExcelWriter('Jobs_output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet1', index=False)
col_auto_scale(writer.sheets['sheet1', df])
writer.save()
