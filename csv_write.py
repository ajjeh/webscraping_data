from bs4 import BeautifulSoup
import requests
import lxml
import csv

url = requests.get('https://coreyms.com/').text
# print(url)
bs = BeautifulSoup(url, 'lxml')
# print(bs.prettify())
main_article = bs.find_all('article')

csv_file = open('extracted_site.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Topic', 'Description', 'Published By', 'Video Link'])

for article in main_article:
  
  heading = article.h2.a.text
  print(heading)
  describe = article.find('div', class_='entry-content').p.text
  print(describe)
  published = article.find('p', class_='entry-meta').text.replace('Leave a Comment', '')
  print(published)

  # Check if the there's a link or not
  try:
    # extracting the youtube link.
    vid_link = article.find('iframe', class_='youtube-player')['src']
    # Obtaining the video ID
    vid_id = vid_link.split('/')[4]
    vid_id = vid_id.split('?')[0]
    # full link generation
    yt_link = f'https://youtube.com/watch?v={vid_id}'
    
  except Exception as e:
    yt_link = "No Video Link"

  print(yt_link)
  print('\n')

  csv_writer.writerow([heading, describe, published, yt_link])

csv_file.close()

  
  
  
  
  
  
