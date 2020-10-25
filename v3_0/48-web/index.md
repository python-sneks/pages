# Web Data

[Download slides](Web%20Data.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Web Data"
src="https://www.youtube.com/embed/lNLglfeqIAs?feature=oembed&amp;rel=0" ></iframe>


#### The Internet is Great

One of the reasons the internet is great is that it makes it easy to share data.
This data can be access programmatically and processed in a program.
Most modern programming languages, like Python, make it easy to access web-based data.

> A picture diagramming the internet as a series of connected globes and *things* is shown - there are many kinds of things, like fish and flowers and hands and DNA and printers and more.  
> These things represent different sources of data in a network.

#### Internet as a Dictionary

The internet can be seen as a giant Dictionary being used as a Record.
You access URLs (which are strings) and get back web pages (which are also strings).
This simplifies a tremendous number of very complex pieces of hardware and software, but this is the result at the end of the day.
Look up a URL, get some string data back.
We'll use a library that makes it just this easy in Python.

> A laptop is shown on the left, and the connected internet picture from before is shown on the right.  
> An arrow points from the laptop to the network with a label that says "URL (request)".  
> An arrow points from the network to the laptop with a label that says "Data (response)".

#### Requests

There are many ways to retrieve data from the internet.
The Requests library is one such tool.
This library is not part of the standard library, but comes with Anaconda.
To get started with the Requests module, we begin by importing it.

```python
import requests
```

#### A Basic Request

The Requests module has a number of useful functions, but in this lesson we only need one: get.
The get function consumes a URL as a string, and returns a Response object.
This response object can be a confusing thing at first, but it is actually very easy to use.

```python
import requests

response = requests.get("https://example.com")
```

#### Text

To get the webpage as a string of data, you can use the "text" attribute of the Response object.
Keep in mind that most websites are written in a language called HTML, which can be tricky to parse.
So for now, we'll access simple text websites.

```python
import requests

response = requests.get("https://pastebin.com/raw/Kt3Xb4pL")

website = response.text

print(website)
```

> The `website` variable will have the text of the website as a string.

#### JSON

If the text content we retrieve from the website happens to be in the JSON format, Requests has a simple way to process it using the JSON method.
Confusingly, JSON is a method call instead of an attribute, so make sure you DO use parentheses with it (unlike the "text" attribute).
Here, we use a website that returns the current date and time as a JSON object.

```python
import requests

response = requests.get("http://date.jsontest.com/")

data = response.json()

print(data['date'])
```

> The URL shown opens to a web page that reads:

```
{
  time: "05:13:11 PM",
  milliseconds_since_epoch: 1506186791975,
  date: "09-23-2017"
}
```

> When you run the code shown, you get the following output:

```
09-23-2017
```

> An annotation points out, don't miss the parentheses for the `response.json()` call!

#### The Internet is Hard

Connecting to the internet can be problematic.
Websites go down, URLs change, your internet can get disconnected, and many other issues are possible.
Usually, you should avoid repeatedly accessing web data if you can help it.
Instead, you should download a file directly and use that.
Still, accessing websites programmatically is a frequent tool in many real-world problems.

> A list of common errors is shown next to a screenshot of a broken webpage:

* Website is down
* URL changed
* Data format changed
* Connection failed
* Connection is slow
* ...
