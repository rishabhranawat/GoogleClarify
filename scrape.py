from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://timesofindia.indiatimes.com/international-home').read()
soup = BeautifulSoup(r)


letters = soup.find_all("a")
print type(letters)
print type(letters[0])
lobbying = {}
for element in letters:
	print element


