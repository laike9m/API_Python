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

On the next line, print `"TEASER: "` plus `story['teaser']['$text']`  **(注：teaser=“片头”,即新闻概要)**

On a separate line, check to see if `'byline'`**(署名)** is in story.  
If so, print `"BYLINE: "` plus `story['byline'][0]['name']['$text']`**(打印第一个作者的名字)**

Not all stories have show (program) metadata, so we'll check that by looking for the `'show'` key.**(节目信息,如果这条新闻被直播过)**

Every NPR story in the API has a web URL for its page location on NPR.org, which is contained in the `'link'` resource.**(NPR网站上该新闻的地址)**

Like the byline resource, show and link have lists as their value. The show resource contains information about the air date of a story and the program name, which is `['show'][0]`.

The 'link' resource always contains more than one URL, but we want the web page URL, which is the first one, `['link'][0]`.

Since we required `image` and `audio` in the `requiredAssets` parameter in our API call, we won't check for those resources. But not all images have a `caption` or `credit`, so we'll use `in` to validate for those.

The image resource can contain more than one image. The first one, `['image'][0]` is the primary and the one we'll be working with.

Likewise, a stories audio resource may contain more than one audio file. The primary audio is given as `['audio'][0]`.

Ok, now we're ready to print the story text. We won't check for it since we required `text` in our API call.

Story text is given as an array of `text` objects. We need to iterate over them and print each paragraph.

The Story API offers two types of text, plain text in the text resource, and text that contains HTML hyperlinks in the `textWithHtml` resource. We're going to print out the text that contains HTML formatting.

<br />
#### Custom Feeds and Podcasts
The Story API also makes it a snap to create custom RSS and podcast feeds.

In fact, one of the very first apps built on top of the Story API was the "Mix Your Own Podcast" generator (Fun fact: the team wanted to call it "Roll Your Own Podcast", but the metaphor didn't fly.)

We're going to make a simple version of that very same app. Let's start by making a custom podcast of music topic stories that contain the word "banjo".

Here's something you didn't know: the `id` parameter can accept more than one value!

We'll allow the user to specify more than one NPR ID, delimited by commas, to blend many kinds of stories together into a custom podcast.

When we query against more than one ID, **the API's default action is to perform an `And` (intersection) and only return stories that belong to every topic specified**. We want stories that match one or more of the topic IDs we include, so we'll **set the `action` parameter to `Or` to perform a Union**.

We haven't learned how to query the API by search string yet, but for now let's ask for user input and make sure we have at least either a list of IDs or a search string to work with.

Finally, we're going to introduce yet another query parameter that is excellent for building custom fields. The `title` parameter lets you -- wait for it -- specify a custom title for your podcast or RSS feed.

We need to check to see if the user passed one or more NPR IDs as a comma-delimited string, and if so, we need to append `'&id='` plus the NPR ID(s) to the end of our API call.

We also need to check whether the user gave us a `search_string`. If so, we'll call `quote()` on the search string to escape any spaces or special characters. Then, we'll append the search string to our `url` query string as the value of `'&searchTerm='`.

Finally, there's the title we stored in `feed_title`. The XML title element is what displays when you're looking at an RSS reader, smart phone, or mp3 player, so it's really useful. Title is an optional parameter in the Story API. We'll need to use `quote()` to escape `feed_title` too. If we have a title we'll append it to `url` as the value of `&title=`

Now let's make some custom podcasts! Your code will prompt you for NPR IDs. You can choose some of the ones below or pick a few from the <a href='http://www.npr.org/api/mappingCodes.php'>mapping index.</a>  
`1001`: News main topic    
`1004`: World topic    
`1032`: Books topic  
`1039` : NPR Music  
`1128` : Health topic  
`1014`: Politics topic  
`13` : 'Fresh Air' program  
`94427042` : 'Planet Money'  
`3850482` : stories by Neda Ulaby  

We can easily modify our app to output an RSS feed with a few minor edits. We'll want stories with text. The Story API also exports valid RSS XML.

Edit the `url` we use to call the API.Change the output format to `rss`.Instead of requiring stories with audio, require stories with text.Hit Save & Submit Code and follow the prompts to output your valid RSS feed XML.