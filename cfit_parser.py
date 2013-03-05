from bs4 import BeautifulSoup
import urllib2

url = 'http://crossfit.com'

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()

soup = BeautifulSoup(data)
list = soup.findAll('div')#, attrs={'class':'blogbody'})

print soup