import urllib2, re
import simplejson

from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi()  # assumes environment variables are set.

menCounter = 0
womenCounter = 0

counter = 0
while(counter != 100):
	if(counter%4 == 0):
		url_string = 'https://ajax.googleapis.com/ajax/services/search/images?'+'v=1.0&q=hackathons&userip=INSERT-USER-IP&start='+str(counter)
		print url_string
	
	counter +=4
	url = (url_string)

	request = urllib2.Request(url, None, {})
	response = urllib2.urlopen(request)

	# Process the JSON string.
	results = simplejson.load(response)

	for i in range(0, len(results), 1):
		try:
			resp =results.get('responseData').get('results')[i].get('url')
			values = clarifai_api.tag_image_urls(resp)
			tags =  values.get('results')[0].get('result').get('tag').get('classes')
			for each in tags:
				if(each == "men" or each == "boy" or each == "man"):
					menCounter += 1
				elif(each == "women" or each == "girl" or each == "woman"):
					womenCounter += 1

		except:
			pass


# now have some fun with the results...
print(menCounter)
print(womenCounter)


