import requests
from urllib.parse import quote

key = "API_KEY"
url = 'http://api.npr.org/query?apiKey='
url += 'MDEyNTM0MTI5MDEzODM2NjY1NzgxODZlOQ001'
url += "&numResults=3&action=Or&requiredAssets=audio&format=Podcast"

npr_id = input("Enter comma-separated NPR IDs or leave blank.")
search_string = input("Enter your search query or leave blank.")
feed_title = input("What's your feed title?")

if npr_id or search_string:
    input("Hit enter to download your podcast.")
    
    if npr_id:
        url+= "&id=" + npr_id
        
    if search_string:
        url += "&searchterm=" + quote(search_string)
    
    if feed_title:
        url += '&title=' + quote(feed_title)
        
    response = requests.get(url)
    output = str(response.content)
    my_feed = open('my_feed.xml', 'w')
    my_feed.write(output)
    my_feed.close()
else:
    print("You must enter an NPR ID, a search term, or both.")
    