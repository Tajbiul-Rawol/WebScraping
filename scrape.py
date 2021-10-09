from bs4 import BeautifulSoup

#scraping from a local html file

with open('Index.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    card_containers = soup.find_all('div', class_="container")

    for card_container in card_containers:
        person_name = card_container.h4.b.text
        position = card_container.p.text
        print("Name : " + person_name +"\n"+ "Job : " + position +"\n")
