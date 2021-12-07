import requests
from bs4 import BeautifulSoup


links = []

def get_links(url):


    website = requests.get (url)
    website_text = website.text
    soup = BeautifulSoup (website_text)
        
    for link in soup.find_all ('a'):
        links.append (link.get ('href'))
    
    for link in links:
        print(link)

    print(len(links))


# get_links('https://www.pornhub.com/')

i = 2

for i in range(0,10):
    get_links('https://www.pornhub.com/' + 'video?page=' + str(i))
    i= i+1





with open ("C:\\Users\\botond\\Documents\\programozás\\pornhub roulette\\links.txt", "w") as f:
        f.writelines(str(links))

