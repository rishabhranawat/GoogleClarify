import urllib
from bs4 import BeautifulSoup

list_of_images = BeautifulSoup(urllib.urlopen('http://www.gardensafari.net/english/squirrels.htm'))
menCounter = 0
womenCounter = 0
for img in list_of_images.find_all("img", src=True):
	print(img["src"])
	try:
		values = clarifai_api.tag_image_urls('http://www.gardensafari.net/english/squirrels.htm'+img["src"])
		tags =  values.get('results')[0].get('result').get('tag').get('classes')
		for each in tags:
				if(each == "men" or each == "boy" or each == "man"):
					menCounter += 1
				elif(each == "women" or each == "girl" or each == "woman"):
					womenCounter += 1
				print each

	except:
		pass



## the code above just prints the link;
## if you want to actually download, set the flag below to True
'''
import urllib, re

source = urllib.urlopen('http://www.gardensafari.net/english/squirrels.htm//pics/eekhoorns/eekhoorn6.jpg').read()

## every image name is an abbreviation composed by capital letters, so...
m = re.findall('.*?\\.(?i)(jpg|jpeg|png|gif|bmp|tif|tiff)', source)

for link in re.findall('.*?\\.(?i)(jpg|jpeg|png|gif|bmp|tif|tiff)', source):
    print link
actually_download = False
if actually_download:
    filename = link.split('/')[-1]
    urllib.urlretrieve(link, filename)
'''