import requests 
from bs4 import BeautifulSoup

r = requests.get('https://butterfly-conservation.org/uk-butterflies/a-to-z')
soup = BeautifulSoup(r.text)
links = soup.find_all('a')

for link in links:
    print(link.attrs.get('href'))

hrefs = [link.attrs.get('href') for link in links]
butterfly_pages = hrefs[39:100]
urls = ['https://butterfly-conservation.org/' + page for page in butterfly_pages]
