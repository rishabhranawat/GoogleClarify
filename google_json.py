import urllib2, re
import simplejson

from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi()  # assumes environment variables are set.

url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
       'v=1.0&q=nurse&userip=INSERT-USER-IP&start=0')

request = urllib2.Request(url, None, {})
response = urllib2.urlopen(request)
menCounter = 0
womenCounter = 0
# Process the JSON string.
results = simplejson.load(response)

for i in range(0, len(results), 1):
	resp =results.get('responseData').get('results')[i].get('url')
	
	try:
		values = clarifai_api.tag_image_urls(resp)
	except:
		pass
	tags =  values.get('results')[0].get('result').get('tag').get('classes')
	for each in tags:
		if(each == "men" or each == "boy" or each == "man"):
			menCounter += 1
		elif(each == "women" or each == "girl" or each == "woman"):
			womenCounter += 1
		print each
# now have some fun with the results...

print(menCounter)
print(womenCounter)


