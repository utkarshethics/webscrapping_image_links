from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)')
soup = BeautifulSoup(html, 'html.parser')
images = soup.find_all('img', {'src':re.compile('.jpg')})
for image in images:
    print(image['src'] + '\n')

