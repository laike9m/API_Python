import requests
import os
import re

class FetchNews():

    url = 'http://api.npr.org/query?apiKey=' 
    key = 'MDEyNTM0MTI5MDEzODM2NjY1NzgxODZlOQ001'
    # http://www.npr.org/api/mappingCodes.php
    
    topics = {
        'Asia': 1125,
        'Education': 1013,
        'Environment': 1025,
        'Politics': 1014,
        'Technology': 1019,
        'Sports': 1055,
        'Economy': 1017,
        'U.S.': 1003,
        'Religion': 1016,
        'Books': 1032,
    }
    
    def __init__(self):
        #base url + the apiKey param
        self.url = self.url + self.key + '&format=json'
        for topic in self.topics.keys():
            0 if os.path.exists(topic) else os.mkdir(topic)

    
    def print_json(self, json_obj):
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
            
            for p in story['text']['paragraph']:
                print(p['$text'] + ' \n')
        
    
    def dump(self, f, story, full_info=False):
        if full_info:
            f.write("TITLE: " + story['title']['$text'] + "\n")
            f.write("DATE: "    + story['storyDate']['$text'] + "\n")
            f.write("TEASER:"    + story['teaser']['$text'] + "\n")
            
            if 'byline' in story:
                f.write("BYLINE: " + story['byline'][0]['name']['$text'] + "\n")
            
            if 'show' in story:
                f.write("PROGRAM: " + story['show'][0]['program']['$text'] + "\n")
            
            f.write("NPR URL: " + story['link'][0]['$text'] + "\n")

            if 'caption' in story:
                f.write("IMAGE CAPTION: ", story['image'][0]['caption']['$text'] + "\n")
            
            if 'producer' in story:
                f.write("IMAGE CREDIT: " + story['image'][0]['producer']['$text'] + "\n")

        for p in story['text']['paragraph']:
            try:
                f.write(p['$text'] + '\n')
            except KeyError:
                pass    # 有的段就是一个数字
    
    
    def search(self, query):
        '根据searchTerm进行搜索'
        0 if os.path.exists('search_result') else os.mkdir('search_result')
        url = self.url + query
        self.fetch(url, 'search_result')
        
    
    def fetch(self, url ,topic):
        #open our url, load the JSON
        response = requests.get(url)
        json_obj = response.json()
        
        #parse our story
        for story in json_obj['list']['story']:
            title = story['title']['$text']
            title = re.sub(r'[<>"*\\/|?]', '', title)   # 标题中的? -> '',: -> -
            title = re.sub(':', '-', title)
            print('fetching ' + title + '...')
            f = open(os.path.join(topic, title+'.txt'), 'wt', encoding='utf-8')
            self.dump(f, story)
            f.close()
    
    
    def fetch_topic(self, topicID=None, amount=20):
        'npr 每次最多抓20条, 所以需要设定startNum实现超过20条新闻的抓取'
        if topicID:
            if type(topicID) is int:
                url = self.url
                url += '&numResults=%s&id=%s&requiredAssets=text' % (amount, topicID)
                print('Fetching topic ' + str(topicID) + '...')
                0 if os.path.exists(str(topicID)) else os.mkdir(str(topicID))
                if amount <= 20: 
                    url = self.url + '&numResults=%s&id=%s&requiredAssets=text' % (amount, topicID)
                    self.fetch(url ,str(topicID))
                else:
                    N = amount//20  # 需要抓取的次数
                    for count in range(N):
                        startNum = count * 20 + 1
                        url = self.url + '&startNum=%s&numResults=20&id=%s&requiredAssets=text' % \
                              (startNum, topicID)
                        self.fetch(url, str(topicID))
            else:
                print('请输入代表类别的数字ID')
        else:
            for topic in self.topics.keys():
                try:
                    idnum = self.topics.get(topic)    
                except:
                    print('topic not found !')
                    
                print('Fetching topic ' + topic + '...\n\n')
                
                if amount <= 20: 
                    url = self.url + '&numResults=%s&id=%s&requiredAssets=text' % (amount, idnum)
                    self.fetch(url, topic)
                else:
                    N = amount//20  # 需要抓取的次数
                    for count in range(N):
                        startNum = count * 20 + 1
                        url = self.url + '&startNum=%s&numResults=20&format=json&id=%s&requiredAssets=text' % \
                              (startNum, idnum)
                        self.fetch(url, topic)
                
            
if __name__ == '__main__':
    fetch_news = FetchNews()
    fetch_news.fetch_topic(topicID=None, amount=200)  