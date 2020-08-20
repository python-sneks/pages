
[Download slides](Dictionary%20Operations.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/i9edWrgsn7Q?feature=oembed&amp;rel=0" 
></iframe>


#### Dictionary Operations

Dictionaries, like lists and strings, have several useful built-in operations we can use.
Altough there are many more, we will learn about membership testing, changing dictionary state, and iteration.

* Membership testing
* Changing dictionary state
* Iteration

#### Membership Test

Dictionaries, like lists or strings, are sequences.
They can possess any number of key-value pairs.
You can test if a specific key is in a dictionary using the in operator, the same way you would test for lists or strings.

```python
>>> pets = {"Klaus": "dog",
            "Pumpkin": "cat",
            "Wrex": "hamster"}

>>> "Klaus" in pets
True
>>> "Spot" in pets
False
>>> "dog" in pets
False
```

#### Changing Dictionary State

Dictionaries, like lists, are mutable.
Therefore, we can freely change the value associated with a key.
Visually, it's just like changing the value associated with a variable, just with the square brackets and key after the dictionary.
In this example, we update each key with a new value.

```python
##### Before
>>> person = {"age": 23,
              "name": "Ellie Cayford",
              "married?": False}
##### Updates
>>> person["married?"] = True
>>> person["name"] = "Ellie Bart"
>>> person["age"] = 1 + person["age"]
##### After
>>> person
{"married?": True, 
 "name": "Ellie Bart", 
 "age": 24}
```

#### Iteration

Dictionaries are a sequence of key/value pairs. 
Therefore, you can iterate through them like a list.
However, there are three different ways to iterate through them:
Through their keys, their values, or their keys and values at the same time.
Notice how this last approach gives us the key and value at the same time!

```python
# Each key one at a time
for a_key in a_dict:
    pass

# Each value one at a time
for a_value in a_dict.values():
    pass

# Each key and value together at a time
for a_key, a_value in a_dict.items():
    pass
```

#### Terminology

A final minor note about dictionaries: dictionaries are also sometimes known as maps, tables, or hashes.
Although there are subtle differences in this terminology, the idea is still roughly the same each time.

> The words "Dictionary", "Map", "Table", and "Hash" are shown to indicate their equivalence.

#### Vocabulary

* Dictionary (Map, Table, Hash)
* Key
* Value
* Key/Value Pair
* Dictionary Literal
* Dictionary Access, Dictionary Lookup
* KeyError