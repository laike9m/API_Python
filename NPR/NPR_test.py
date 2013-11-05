import requests
from urllib.request import urlopen
from json import load 

url = 'http://api.npr.org/query?apiKey=' 
key = 'API_KEY'
url = url + key
url += '&numResults=3&format=json&id='
url += input("Which NPR ID do you want to query?")

response = requests.get(url)

#response = urlopen(url)

json_obj = load(response.content)

for story in json_obj['list']['story']:
    print(story['title']['$text'])
