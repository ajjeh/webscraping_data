from bs4 import BeautifulSoup

with open('web.html', 'r') as html_file:
    content = html_file.read()

    bsoup = BeautifulSoup(content, 'lxml')

    services_cards = bsoup.find_all('div', class_='col-sm-6')
    for services in services_cards:
        # print(services.h4)
        service_name = services.h4.text
        service_desc = services.p.text.split()[-1]

        # print(service_name)
        # print(service_desc)
        print(f'{service_name} has this word {service_desc}' )