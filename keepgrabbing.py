import urllib2
#import urllib
from BeautifulSoup import BeautifulSoup


page = urllib2.urlopen("https://laplanetebleue.com/podcast")
soup = BeautifulSoup(page)
ul = soup.find('ul',attrs={"id":"playlist"})
listHref = []
listName = []
dict = {}
for a in ul.findAll('a'):
    name = a['id'].split('-')[0]
    if name in dict:
        print name+ ": Already in dictionnary"
    else:
        dict[name] = a['href']

print dict

#urllib.urlretrieve ("http://www.example.com/songs/mp3.mp3", "mp3.mp3")
