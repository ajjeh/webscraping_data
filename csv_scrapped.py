from bs4 import BeautifulSoup
import requests


def scrap_job():

    url = requests.get("https://coreyms.com/").text
    # print(url)

    bsp = BeautifulSoup(url, "lxml")
    hd_tag = bsp.find('article')

    print(hd_tag.prettify())



scrap_job()
