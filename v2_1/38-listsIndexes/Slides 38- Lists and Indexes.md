# &icon-ms-ppt; Slides

[Download slides](https://udel.instructure.com/files/75542509/download){: .instructure_file_link .instructure_scribd_file }

# &icon-video; Video

<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/QlMdDPuZeEc?feature=oembed&amp;rel=0" 
></iframe>

# &icon-document; Transcript

#### Lists and Indexes

So far, we have iterated through a list using the for-each syntax to get each value of the list.
In many languages, indexes are used to access the values of a list.
The index of the list are the integers, starting from 0 and counting up, that uniquely identify each element.

> Arrows extend from these lists indicating that they might continue on.

```python
[10, 10, 20, 1, ...]
```

| 10 | 10 | 20 | 1 | ... |
|----|----|----|---|-----|

> Each cell of the table is marked with ascending numbers: 0, 1, 2, 3, ...

#### Value vs. Index Style

The top code shown here is the preferred way to process a list, where we iterate through each value.
However, you can also iterate by using a combination of the range and len functions, as shown here.
Both the Value style and the Index style shown will print the same result.

```python
names = ["Adam", "Betty", "Clarice"]
    
# Value style
for name in names:
    print(name)


# Index style
for i in range(len(names)):
    print(names[i])
```

#### Range and Len Built-ins

The `range` and `len` functions are built-in to Python.
The `len` function consumes a list or other iterable and produces an integer representing its length.
The `range` function consumes an integer and produces a list of integers from 0 up till that number.
You can combine these two functions to create the list of indexes corresponding to a list.

```python
>>> grocery_list = ['Bread', 'Ham', 'Eggs']

>>> number_of_groceries = len(grocery_list)
>>> number_of_groceries
3

>>> grocery_indexes = range(3)
[0, 1, 2]
```

#### Indexes vs. Values

So when do you use indexes and when do you use values?
Usually, you should stick to value style unless you have an explicit reason to use indexes.
Indexes allow more flexibility and are necessary for certain kinds of specialized algorithms.
However, they require more operations and are more complex to reason about.

1. Indexes allow more flexibility
2. Values require fewer operations
3. Values are less complex
