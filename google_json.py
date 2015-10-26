import urllib2
import simplejson

from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi()  # assumes environment variables are set.

url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
       'v=1.0&q=google%20workers&userip=INSERT-USER-IP&start=8')

request = urllib2.Request(url, None, {})
response = urllib2.urlopen(request)
menCounter = 0
womenCounter = 0
# Process the JSON string.
results = simplejson.load(response)

for i in range(0, len(results), 1):
	values = clarifai_api.tag_image_urls(results.get('responseData').get('results')[i].get('url'))
	tags =  values.get('results')[0].get('result').get('tag').get('classes')
	for each in tags:
		if(each == "men"):
			menCounter += 1
		elif(each == "women"):
			womenCounter += 1
		print each
# now have some fun with the results...

print(menCounter)
print(womenCounter)