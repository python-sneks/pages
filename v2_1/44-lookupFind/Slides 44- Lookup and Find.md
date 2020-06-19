
[Download slides](https://udel.instructure.com/files/75688988/download){: .instructure_file_link .instructure_scribd_file }


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/4vVoa94yBu4?feature=oembed&amp;rel=0" 
></iframe>


#### Lists vs. Dictionaries

Both lists and dictionaries are collections of data.
You can use them to store and retrieve data later.
However, which one you use can have performance implications.

> A scale shows that Lists and Dictionaries have ups and downs.

#### Finding in a List

Say we have a list of strings that represent names.
If we want to determine whether a particular string is in the list, we must walk through each element.
If there are 10 strings, this will not take long.
But what if there are many, many strings, like in the University's directory?
Finding a string in a list will take longer when there are more elements.

```python
names = ["Alice", "Bob", ..., "Klaus"]

# Slow
for name in names:
    if name == "Klaus":
        ...
```

> An annotation points out that the list is meant to be massive, with millions of elements.

#### Looking up in a dictionary

However, if you use a dictionary to store names (perhaps mapped to their address or grade), then you can look up keys instantly.
On average, dictionaries' lookup does not take longer no matter how many elements there are.
This is a major advantage of dictionaries over lists.

```python
grades = {"Alice": 99,
          "Bob": 45,
          ...
          ...
          "Klaus": 100 }

# Fast
grades["Klaus"]
```

> An annotation points out that the dictionary is meant to be massive, with millions of elements.

#### Choosing Data Structures

Lists are great when you need to go through many items in a specific order.
Dictionaries are great when you need to lookup a single item.
Think carefully about your use case, and choose an appropriate data structure.

* Lists - If you need to process everything
* Dictionaries - If you need one specific thing given another
