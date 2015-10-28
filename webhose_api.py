import unirest

response = unirest.get("https://webhose.io/search?token=237efe51-29d7-4a3e-bddf-576cd8605ff5&format=json&size=100&q=%22girls%20code%22",
    headers={
    "Accept": "text/plain"
    }
)

for i in range(0, 99, 1):
	print response.body.get("posts")[i].get("thread").get("url")
