
[Download slides](Dictionary%20Patterns.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/yjp04tHak-4?feature=oembed&amp;rel=0" 
></iframe>


#### Using Dictionaries
Dictionaries are very useful for a broad number of applications.
However, it can be tricky to understand how to use them.
In this lesson, you will see a couple common patterns for how to use Dictionaries.

* Lookup
* Counting

#### Lookup Pattern

Dictionaries can be used to quickly convert one value into another.
Consider the example here; this dictionary can be used to words to their abbreviation.
Note that this could have also been implemented as a function with an IF statement.
However, if you are only looking up a single value, then the dictionary will be much easier and faster.
Although this example uses strings, you can really map any type of data to any other type of data in a lookup dictionary.

```python
abbreviations  = {"Virginia": "VA", 
                  "Delaware": "DE", 
                  "Maryland": "MD",
                  "North Carolina": "NC"}
                  
>>> abbreviations["Virginia"]
'VA'
```

#### Counting Pattern

We have previously used the Counting pattern to count the number of occurrences of an item in a list.
But what if we want to count the occurrences for each possible item in a list, without knowing the items before hand?
By adding in a dictionary, we can do just that.
The counting pattern results in a dictionary of any kind of keys mapped to integers.
Notice that dictionary access can be used to update a value, in addition to getting a value.
When the dictionary access occurs on the left side of an assignment, the value associated with that key will be replaced.
Moreover, you can see that we are using a variable to access elements, instead of a string literal.

```python
a_list = [1, 3, 1, 1, 3, 2, 1, 3, 2, 3]
counts = {}
for item in a_list:
    if item in counts:
        counts[item] = counts[item] + 1
    else:
        counts[item] = 1
```
