import requests

#base url + the apiKey param
url = 'http://api.npr.org/query?apiKey=' 
key = 'MDEyNTM0MTI5MDEzODM2NjY1NzgxODZlOQ001'
url = url + key
url += '&numResults=1&format=json&id=1007'
url += '&requiredAssets=text,image,audio'

#open our url, load the JSON
response = requests.get(url)
json_obj = response.json()

#parse our story
for story in json_obj['list']['story']:
    print("TITLE: " + story['title']['$text'] + "\n")
    print("DATE: "    + story['storyDate']['$text'] + "\n")
    print("TEASER:"    + story['teaser']['$text'] + "\n")
    
    if 'byline' in story:
        print("BYLINE: " + story['byline'][0]['name']['$text'] + "\n")
    
    if 'show' in story:
        print("PROGRAM: " + story['show'][0]['program']['$text'] + "\n")
    
    print("NPR URL: " + story['link'][0]['$text'] + "\n")
    print("IMAGE: " + story['image'][0]['src'] + "\n")
    
    if 'caption' in story:
        print("IMAGE CAPTION: ", story['image'][0]['caption']['$text'] + "\n")
    
    if 'producer' in story:
        print("IMAGE CREDIT: " + story['image'][0]['producer']['$text'] + "\n")
    
    print("MP3 AUDIO: " + story['audio'][0]['format']['mp3'][0]['$text'] + "\n")
    
    # loop through and print each paragraph, this is textwithhtml
    #for paragraph in story['textWithHtml']['paragraph']:
        #print(paragraph['$text'] + " \n")
    
    # print plain text, this is what we need
    for p in story['text']['paragraph']:
        print(p['$text'] + ' \n')