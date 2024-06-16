import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url= input('Enter- ')
html= urllib.request.urlopen(url).read()
soup= BeautifulSoup(html, 'html.parser')
for line in soup:
    words=line.decode().split(_)

tags= soup('a')
for tag in tags:
    print('TAG:',TAG)
    print('URL:',tag.get('href',None))
    print('Contents:',tag.contents[0])
    print('Attrs:',tag.attrs)

    