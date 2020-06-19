# &icon-ms-ppt; Slides

[Download slides](https://udel.instructure.com/files/79422106/download){: .instructure_file_link .instructure_scribd_file }

# &icon-video; Video

<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/3hUbAo6m2G8?feature=oembed&amp;rel=0" 
></iframe>

# &icon-document; Transcript

#### Record Pattern

With the Record Pattern, dictionaries become a useful way to hold data that represents a single complex thing.
In the example below, we represent a person using a dictionary with 3 keys.
Records should always use strings as keys, and every instance of that type of record should have the same keys.
The values will be different across instances, but the values' types will always be the same type as other records that represent that complex thing.

```python
first_person = {"name": "Cory", 
                "age": 27, 
                "has a dog?": True}

second_person = {"name": "Adam", 
                 "age": 45, 
                 "has a dog?": False}

>>> first_person["name"]
'Cory'
>>> second_person["age"]
45
```

#### Record Types

A major advantage of using records is that we can be more precise with our types.
We can create a new type to represent records using a dictionary literal that
maps string keys to types.
Once defined, we can use that record anywhere we would use another type.
In this example, we have created a `Person` record.
A Person dictionary record must always have the keys `"age"`, `"name"`, and `"has a dog?"`, with the exact same spelling and capitalization.

```python

Person = {"name": str, "age": int, "has a dog?": bool}

def make_person(n: str, a: int, d: bool) -> Person:
    return {
        "name": n,
        "age": a,
        "has a dog?": d
    }
```

#### Types vs Instances

A Record is a dictionary with a very specific structure.
We can specify that structure using a Record Type.
When we create a new Record, we say that we have created an instance of the Record.

```python

# Record type
Cup = {"size": int, "color": str}

# Record instances
black_mug = {"size": 6, "color": "black"}
white_cup = {"size": 12, "color": "white"}

```

#### Record Functions
We only need record types when we are defining functions that work with record instances.
We use the record types to give extra information in the parameter types and return types.
They have no actual impact on the code, they are just extra information for any humans trying to understand the program.

```python

# Make a new Cup
def make_cup(size: int, color: str) -> Cup:
    return { "size": size, "color": color }


# Get information about a Cup
def get_size_in_feet(a_cup: Cup) -> float:
    return a_cup["size"] / 12
def is_white_cup(a_cup: Cup) -> bool:
    return a_cup["color"] == "white"


```