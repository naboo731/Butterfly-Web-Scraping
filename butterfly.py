# import libraries needed: requests and beautifulsoup.
import requests 
from bs4 import BeautifulSoup

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
