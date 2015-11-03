from alchemyapi import AlchemyAPI
import urllib2, re
import json
import simplejson

'''
menCounter = 0
womenCounter = 0
alchemyapi = AlchemyAPI()
counter = 0
while(counter != 100):
	if(counter%4 == 0):
		url_string = 'https://ajax.googleapis.com/ajax/services/search/images?'+'v=1.0&q=facebook%20workers&userip=INSERT-USER-IP&start='+str(counter)
	
	counter +=4
	url = (url_string)

	request = urllib2.Request(url, None, {})
	response2 = urllib2.urlopen(request)

	# Process the JSON string.
	results = simplejson.load(response2)

	for i in range(0, len(results), 1):

			image_url =results.get('responseData').get('results')[i].get('url')
			print('Processing url: ', image_url)
			print('')

			response = alchemyapi.imageTagging('url', image_url)
			print(response['status'])
			if response['status'] == 'OK':
			    print('## Response Object ##')
			    print(json.dumps(response, indent=4))

			    print('')
			    print('## Keywords ##')
			    for keyword in response['imageKeywords']:
			        print(keyword['text'], ' : ', keyword['score'])

			    print response
			    print('')
			else:
			    print('Error in image tagging call: ', response['statusInfo'])

'''

negative = 0
positive = 0
neutral = 0

import unirest
alchemyapi = AlchemyAPI()

counter = 0
while(counter != 4):

	url = ('https://ajax.googleapis.com/ajax/services/search/web'
	       '?v=1.0&q=Google%20wokrers&start='+str(counter))

	request = urllib2.Request(url, None, {})
	response = urllib2.urlopen(request)

	# Process the JSON string.
	results = simplejson.load(response)
	i = 0
	for i in range(0, len(results.get("responseData").get("results")), 1):
		print results.get("responseData").get("results")[i].get("title")
			response = alchemyapi.entities('text', title, {'sentiment': 1})

		if response['status'] == 'OK':
		    for entity in response['entities']:
		    	if(entity['sentiment']['type'] == 'negative'):
		    		negative += 1
		    	elif(entity['sentiment']['type'] == 'positive'):
		       		positive += 1
		       	else:
		       		neutral +=1
		else:
		    print('Error in entity extraction call: ', response['statusInfo'])
	counter += 4

print negative
print positive
print neutral

'''
import unirest
alchemyapi = AlchemyAPI()

response_m = unirest.get("https://webhose.io/search?token=237efe51-29d7-4a3e-bddf-576cd8605ff5&format=json&size=1000&q=women%20tech",
    headers={
    "Accept": "text/plain"
    }
)

negative = 0
positive = 0
neutral = 0

for i in range(0, 100, 1):
	title = response_m.body.get("posts")[i].get("thread").get("title_full")

	response = alchemyapi.entities('text', title, {'sentiment': 1})

	if response['status'] == 'OK':
	    for entity in response['entities']:
	    	if(entity['sentiment']['type'] == 'negative'):
	    		negative += 1
	    	elif(entity['sentiment']['type'] == 'positive'):
	       		positive += 1
	       	else:
	       		neutral +=1
	else:
	    print('Error in entity extraction call: ', response['statusInfo'])


print negative
print positive
print neutral

'''
