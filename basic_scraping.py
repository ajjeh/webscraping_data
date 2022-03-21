from bs4 import BeautifulSoup

# This will help us open the file and open the file and read the content of the file
with open('web.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    # Creating an instance of bs library.
    bsoup = BeautifulSoup(content, 'lxml')
    # print(bsoup.prettify())

    # Grabbing specific html tags.
    services_html_tags = bsoup.find_all('h4')
    # print(tags)
    for services in services_html_tags:
        print(services.text)
