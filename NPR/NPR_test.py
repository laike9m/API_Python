from urllib.request import urlopen
import requests
from json import load 

url = 'http://api.npr.org/query?apiKey=' 
key = 'MDEyNTM0MTI5MDEzODM2NjY1NzgxODZlOQ001'
url = url + key
url += '&numResults=3&format=json&id='
url += input("Which NPR ID do you want to query?")

r = requests.get(url)
json_obj = r.json()


for story in json_obj['list']['story']:
    print(story['title']['$text'])
