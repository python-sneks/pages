# Dictionaries

[Download slides](Dictionaries.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Dictionaries"
src="https://www.youtube.com/embed/LFnamjuLBig?feature=oembed&amp;rel=0" ></iframe>


#### Dictionaries

Dictionaries are one of the most flexible and useful data structures in programming.
The idea of a dictionary is that they map from keys to values.
Think of it like an actual dictionary: given a word, you can look up its definition.
This lookup has a large number of applications.

> A series of words are mapped to their definitions, as if you were looking in an english langugage dictionary.  
> For example, the word "Aardvark" is next to "A nocturnal burrowing mammal feeding on ants and termites."

#### Dictionary Literals

The syntax for a dictionary literal begins with a pair of curly braces.
Inside of those braces, you will find key/value pairs separated by commas.
Each key is separated from its value with a colon.
The key and the value can be any expression, but are often literal values.
Although not required, each key-value pair is often placed on its own new line.

```python
{
    "A key": "A value", 
    "Another Key": 5, 
    7: True
}
```

> Annotations point out the use of the Curly Brace (`{`), Commas (`,`), and Colon (`:`) symbols.   
> Additional annotations point out the Keys on the left and the Values on the right.

#### Keys

The keys of a dictionary are what we use to look up information.
The keys of a dictionary are unique.
Typically, the keys will be of the same type, although this is not technically a requirement.

```python
{ "Key": "Value" }
```

> A box is drawn around the `"Key"` with an arrow coming into it.

#### Values

Each key is mapped to a value.
With the appropriate key, we can get a desired value.
Values do not have to be unique, unlike keys.
Like keys, the values can be of any type, even if they are not the same.

> A box is drawn around the `"Value"` with an arrow coming out of it.

#### Dictionary Access

The values of a dictionary can be retrieved using dictionary access.
Another similarity between lists and dictionaries is how both use square brackets.
With lists, we used numeric indexes to access elements.
With dictionaries, we use the keys.
Often, the keys will be strings, so often we will see strings inside the square brackets.

```python
# Dictionary literal value assigned to a variable
my_dictionary = {"A key": "A value", 
                 "Another Key": 5, 
                 7: True}

# Dictionary access using the key "A key"
my_dictionary["A key"]
```

> Annotations point out the use of square brackets (`[` and `]`) around the key, next to the dictionary value on the left.

#### Lookups

When we perform dictionary access, we give a key, and the dictionary access expression is replaced with the corresponding value.
If the key is not in the dictionary, a "KeyError" is raised.
A common mistake is to use a value instead of a key, which will also cause a "KeyError".

```python
>>> pets = {"Klaus": "dog",
            "Pumpkin": "cat",
            "Wrex": "hamster"}

>>> pets["Klaus"]
"dog"

>>> pets["Spot"] # KEY ERROR, does not work!

>>> pets["dog"] # KEY ERROR, does not work!
```

> Annotations point out that the last two lines do not work.

#### Not Always Strings

Sometimes keys will be strings, but it turns out that anything can be a key.
If a dictionary maps integers to strings, for instance, then the keys will be integers.
In fact, it is possible for a dictionary lookup to appear just like a list lookup!

```python
>>> levels = {3: "High",
            2: "Medium",
            1: "Low"}

>>> levels[2]
"Medium"

>>> levels[0]        # KeyError, does not work!

>>> levels["High"]   # KeyError, does not work!
```

> Annotations point out that the last two lines do not work.

#### Dictionary Type

When you define a function that consumes or produces a dictionary, we need to specify the type.
If we don't know anything specific about the dictionary's keys and values, we can use the the `dict` type.
However, if we know that the dictionary maps, say, strings to integers, then we can use a dictionary as the type.
The function shown here uses a list of integers to produce a dictionary that maps string keys to integer values.

```python
def make_ratings(ratings: [int]) -> {str: int}:
    return {
        "dog": ratings[0],
        "cat": ratings[1],
        "rat": ratings[2]
    }
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
* Records
* Associations
* Dictionary Literal
* Dictionary Access, Dictionary Lookup
* KeyError
