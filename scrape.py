from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('https://www.linkedin.com/title/engineering-practicum-intern').read()
soup = BeautifulSoup(r)


letters = soup.find_all("Education")
print type(letters)
print type(letters[0])
lobbying = {}
for element in letters:
	print element


