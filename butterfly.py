# import libraries needed: requests and beautifulsoup.
from multiprocessing import process
import requests 
from bs4 import BeautifulSoup
import re
import csv

r = requests.get('https://butterfly-conservation.org/uk-butterflies/a-to-z')
# get request to specific webpage set to variable 'r'.
soup = BeautifulSoup(r.text)
# beautiful soup method takes in the text properities of the get request (i.e. the text on the webpage) and sets to a variable 'soup'.
links = soup.find_all('a')
# find_all method will search for all HTML classifiers passed in in the soup variable. This instance it is searching for all 'a' tags. 

for link in links:
    print(link.attrs.get('href'))
# for loop over all the links or 'a' tags on the webpage. For each link found, it will print the atrribute of the link given the 'href' tag.

hrefs = [link.attrs.get('href') for link in links]
# saving the links to a variable called 'href'.
butterfly_pages = hrefs[39:100]
# specifying we dont want every single link on the page only the ones that pertain to butterflies. Looked at the website and found it was from link 39 to 100.
urls = ['https://butterfly-conservation.org/' + page for page in butterfly_pages]
# created url variable with the base url = 'https://....' and then tack on the page or 'name of butterfly' for each butterfly page there is.

def peel_data_from_element(element):
  just_text = element.text
  return just_text.split(': ')[1]

def get_butterfly(url):
    """Request and parse a single butterfly profile page, return a dict of data"""

    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    h1 = soup.find('h1')
    name = h1.text
    name = name.strip()
    # strips off whitespace at end of name 

    family = soup.find('li', text=re.compile(r'Family:*'))
    size = soup.find('li', text=re.compile(r'Size:*'))
    wing_span = soup.find('li', text=re.compile(r'Wing Span:*'))

    return {'name' : name, 
            'url': url,
            'family': peel_data_from_element(family),
            'wing span': peel_data_from_element(wing_span),
            'size': peel_data_from_element(size)}

def process_each_link(url):
    for url in urls:
       list = get_butterfly(url)
    return list

def write_csv(list):
    csv_content = list
    csv_file = open('butterfly_data.csv', 'w')

    csv_writer = csv.writer(csv_file, delimiter=',')

    for row in csv_content:
        csv_writer.writerow(row)
        print(row['name'], row['url'], row['family'], row['wing span'], row['size'])
    
    csv_file.close()

process_each_link(urls)



