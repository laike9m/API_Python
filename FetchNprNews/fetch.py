import requests
import os
import json
import re

class FetchNews():

    url = 'http://api.npr.org/query?apiKey=' 
    key = 'MDEyNTM0MTI5MDEzODM2NjY1NzgxODZlOQ001'
    # http://www.npr.org/api/mappingCodes.php
    topics = {
        'Asia': 1125,
        'Business': 1006,
        'Education': 1013,
        'Environment': 1025,
        'Politics': 1014,
        'Technology': 1019,
        'Sports': 1055,
    }
    
    def __init__(self):
        #base url + the apiKey param
        self.url = self.url + self.key
        for topic in self.topics.keys():
            0 if os.path.exists(topic) else os.mkdir(topic)

    
    def dump(self, title, text, topic):
        with open(os.path.join(topic, title+'.txt'), 'wt') as f:
            f.write(text)
    
    def fetch(self, url ,topic):
        #open our url, load the JSON
        response = requests.get(url)
        json_obj = response.json()
        
        #parse our story
        for story in json_obj['list']['story']:
            title = re.sub('\?', '', story['title']['$text'])
            print('fetching ' + title + '...')
            f = open(os.path.join(topic, title+'.txt'), 'wt')
            f.write("TITLE: " + story['title']['$text'] + "\n")
            f.write("DATE: "    + story['storyDate']['$text'] + "\n")
            f.write("TEASER:"    + story['teaser']['$text'] + "\n")
            
            if 'byline' in story:
                f.write("BYLINE: " + story['byline'][0]['name']['$text'] + "\n")
            
            if 'show' in story:
                f.write("PROGRAM: " + story['show'][0]['program']['$text'] + "\n")
            
            f.write("NPR URL: " + story['link'][0]['$text'] + "\n")
            #print("IMAGE: " + story['image'][0]['src'] + "\n")
            
            if 'caption' in story:
                f.write("IMAGE CAPTION: ", story['image'][0]['caption']['$text'] + "\n")
            
            if 'producer' in story:
                f.write("IMAGE CREDIT: " + story['image'][0]['producer']['$text'] + "\n")
            
            
            # loop through and print each paragraph, this is textwithhtml
            #for paragraph in story['textWithHtml']['paragraph']:
                #print(paragraph['$text'] + " \n")
            
            # print plain text, this is what we need
            
            for p in story['text']['paragraph']:
                try:
                    f.write(p['$text'] + ' \n')
                except KeyError:
                    pass    # 有的段就是一个数字
            
            f.close()
    
    
    def fetch_topic(self, topic, amount=10):
        for topic in self.topics.keys():
            try:
                idnum = self.topics.get(topic)    
            except:
                print('topic not found !')
            url = self.url
            url += '&numResults=%s&format=json&id=%s&requiredAssets=text' % (amount, idnum)
            print('Fetching topic ' + topic + '...')
            self.fetch(url ,topic)
            
            
if __name__ == '__main__':
    fetch_news = FetchNews()
    fetch_news.fetch_topic('Asia', 10)  