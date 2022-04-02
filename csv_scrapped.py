from bs4 import BeautifulSoup
import requests

site_url = "https://deliveryhero.wd3.myworkdayjobs.com/en-US/talabat/jobs?Job_Application_ID=53615a17124a8101fed4234ac0970000"

with open(site_url, 'r') as site_file:
    
    sp = BeautifulSoup(site_file, 'lxml')
    job_listings = sp.find('li', class_='WH5F WGQO WBAB WOAG')
    
