tutorial from Codecademy

#### Intro to the NPR Story API

Next, we're going to start building our API call, which is a string. The base URL for all story queries is the string `"http://api.npr.org/query"`. All the other control options for our API call are passed in as query string parameters.

The first query string parameter we need to add is `"apiKey"`, which holds our API key. We'll show you how to get your own API key later on. For now, we'll use `'API_KEY'`, which only works inside this course.

The `numResults` parameter specifies the maximum number of stories returned for a query. The default is 10, but we'll just work with three for now.

The Story API outputs many formats, including RSS and podcast XML, which we'll be using in a later lesson. For now, we'll be using JSON, and we specify that with the `format` parameter.

Before we continue, there are two crucial points about the Story API. Once you understand these concepts, working with the Story API is much easier.

First, the Story API always returns NPR stories. Stories always contain at least a title, a date, and a description or what we call a "teaser." Beyond those basics, stories contain other content resources. Some stories have text and images. Stories that aired on NPR programs or podcasts may have audio attached to them. Later, we'll teach you how to request only stories that have audio, text, or images attached. Stories also have metadata ascribed to them, including topic, program, and reporter byline. And that's a good segue...

Second, the Story API is based on numeric IDs, and these are passed in the `id` parameter. Every story on NPR.org has its own **unique ID**. Likewise, every topic, program, music genre, and NPR reporter has its own aggregation ID. If you pass in an ID for a single story, the Story API returns just that story. **If you pass in an aggregation ID, such as a topic, the API returns the most recent stories from that aggregation**.

Ok, let's get back to coding. Let's add the NPR ID 1001, the main news feed, to our API call.

The individual stories in our JSON object are contained in `json_obj['list']['story']`. Use a for loop to iterate over each individual story held there as `story`.

For each story, print its title: `story['title']['$text']`

Try entering a few different NPR ID's:

`1001` : News topic  
`1002` : NPR.org homepage feed  
`1045` : Movies topic  
`1007` : Science topic  
`1032` : Economy topic  
`1039` : NPR Music  
`2` : 'All Things Considered' program  
`5500502` : 'Krulwich Wonders...' blog    
`2101154` : stories by Ari Shapiro  
`93568166` : 'Monkey See' Pop Culture  

<br />
#### Working With Stories
Now, we'll introduce the powerful `requiredAssets` parameter, which forces the API to only return stories that contain the specified content resources.

`requiredAssets` can contain one or more of the following values, separated by a comma:`text`, `image`, or `audio`. The order isn't important. We'll require all three content resources so that we can parse all of them.

Print `"DATE: "` plus `story['storyDate']['$text']`.

On the next line, print `"TEASER: "` plus `story['teaser']['$text']`  
(**注：teaser=“片头”,即新闻概要**)

On a separate line, check to see if `'byline'`(**署名**) is in story.

If so, print `"BYLINE: "` plus `story['byline'][0]['name']['$text']`(**打印第一个作者的名字**)