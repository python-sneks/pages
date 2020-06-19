
[Download slides](https://udel.instructure.com/files/75278300/download){: .instructure_file_link .instructure_scribd_file }


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/gtVituLsJOY?feature=oembed&amp;rel=0" 
></iframe>


#### Doing Stuff with Lists

Once we have data inside of a list, we can do stuff with it.
There are actually many, many operations you can do on a list, so we'll learn about a few of them here.

* Indexing
* Subscripting
* Membership Test
* Appending
* Popping

#### Indexing a List

Much like strings, you can use square brackets to access a specific element of the list.
Notice that the syntax is the same, including the fact that we start counting from zero.
Do not be confused by the square brackets here - when they are first, they are list creation.
When they are second, they are list indexing.

```python
>>> names = ["Alice", "Bob", "Carol"]
# Second element
>>> names[1]
Bob

# First element
>>> [10, 20, 30, 40][0]
10

# Last element
>>> [10, 20, 30, 40][-1]
40
```

#### Subscripting a List

Much like strings, you can use a colon and square brackets to access a range of elements from a list.
The rules are the same as for strings: the first number is the starting index, and the second element is the ending index.

```python
>>> names = ["Alice", "Bob", "Carol"]
# Second until end
>>> names[1:]
["Bob", "Carol"]

# Second until fourth
>>> [10, 20, 30, 40][1:3]
[20, 30]

# Second to last until end
>>> [10, 20, 30, 40][-1:]
[40]
```

#### List Membership

Much like strings, you can ask if a list has a specific value in it.
The `in` operator has a list on the right, and then any kind of value or variable on the left.
There is also a `not in` operator.

```python
>>> names = ["Alice", "Bob", "Carol"]
>>> "Carol" in names
True

>>> "David" not in names
True

>>> "Ellie" in names
False
```

#### Appending to a List

You cannot add elements to a list using the + operator.
Instead, you must call a method of the list, called `append`.
The word "Append" means "add to the end".
Append lets you add one thing to the end of the list.

```
>>> names = ["Alice", "Bob", "Carol"]
>>> names.append("David")
>>> names
['Alice', 'Bob', 'Carol', 'David']
```

> An annotation demonstrates that the following code results in an error, because you cannot add two lists with `+`:

```python
# Wrong!
names + "Ellie"
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "str") to list
```


#### Pop from a List
You can also remove one thing from the end of the list using the "pop" method.
You will not need to do this too often in this course, because removing things
from a list can actually be a little tricky.

```python
>>> names = ["Alice", "Bob", "Carol"]
>>> names.pop()
'Carol'
>>> names
['Alice', 'Bob']
```
