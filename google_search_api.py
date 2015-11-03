import urllib2
import simplejson

# The request also includes the userip parameter which provides the end
# user's IP address. Doing so will help distinguish this legitimate
# server-side traffic from traffic which doesn't come from an end-user.

i = 0






counter = 0
while(counter != 42):

	url = ('https://ajax.googleapis.com/ajax/services/search/web'
	       '?v=1.0&q=Google%20wokrers&start='+str(counter))

	request = urllib2.Request(url, None, {})
	response = urllib2.urlopen(request)

	# Process the JSON string.
	results = simplejson.load(response)

	for i in range(0, len(results.get("responseData").get("results")), 1):
		print results.get("responseData").get("results")[i].get("title")

	counter += 4





'''
try:
	url = ('https://ajax.googleapis.com/ajax/services/search/web'
	       '?v=1.0&q=women&start=0')

	request = urllib2.Request(
	    url, None, {})
	response = urllib2.urlopen(request)

	# Process the JSON string.
	results = simplejson.load(response)
	for i in range(0, len(results), 1):
		print results.get("responseData").get("results")[i].get("title")
		print i
except:
	print ("Nothing")
'''
# now have some fun with the results...
