import requests
from json import load, dumps

#transcript API call URL
apiKey = 'MDEyNTM0MTI5MDEzODM2NjY1NzgxODZlOQ001'
url = 'http://api.npr.org/transcript?apiKey=' + apiKey
url += '&format=json&id=152248901'

response = requests.get(url)
j = response.json()

#print transcript paragraphs
for paragraph in j["paragraph"]:
    print(paragraph["$text"] + "\n")

# uncomment 3 lines below to see JSON output to file
#f = open('output.json', 'w')
#f.write(dumps(j, indent=4))
#f.close()