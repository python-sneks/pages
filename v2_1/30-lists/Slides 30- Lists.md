
[Download slides](https://udel.instructure.com/files/78929706/download){: .instructure_file_link .instructure_scribd_file }


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/xoim3qmDRzo?feature=oembed&amp;rel=0" 
></iframe>


#### Primitives vs. Composites

We have learned about 5 primitive types: Booleans, Integers, Floats, Strings, and the special None.
Python actually has many more types, which are called Composite types.
Composite types are named because they are composed of other types, unlike primitive types.

> Primitive Types:

* Boolean
* Integer
* Float
* String
* None

> Composite Types:

* List

#### Lists

The first composite type is the List type.
A list is a sequence of values.
For instance, you could have a list of numbers, or a list of strings.

```python
[45, 55, 32]
["Apples", "Oranges", "Bananas"]
[True, False, True]
```

#### Lists of X

A "List" is a type, much the same way that Integer is a type.
However, the List will also have an "element type", which is what it is composed of.
So if you have a list of integers, its type is "List" and its element type is "integer".

```python
[45, 55, 32]
```

> An annotation points out that the value above is of type List but has the element type Integer.

#### Defining a List

We create lists using square brackets.
Each value that we want to put into the list is separated by commas.
The square brackets are critical to making this a list; without them it is not a list.

```python
[45, 55, 32]
```

> Annotations point out the use of square brackets on either end of the list, and commas within.

#### Square Brackets

We've seen square brackets used before, when we were subscripting and indexing a list.
Confusingly, Python ALSO uses square brackets for creating lists. 
You might struggle at first figuring out when you're looking at subscripting or list creation.
The key is whether the square brackets come AFTER an expression - that means subscripting.
If the square brackets are on their own, you have a list.

> List Creation

```python
[1, 2, 3]
```

> Indexing

```python
message[0]
```

> An annotation points out that indexing has square brackets AFTER the variable.

#### Empty Lists

A pair of square brackets with nothing between them creates an empty list.
An empty list is like an empty bag: you may not have anything in it, but you still have the bag itself.
Empty lists do not have an element type, until you put something in them.

> On the left side, a pair of square brackets representing an empty list literal value `[]`  
> On the right side, a picture of an empty bag.

#### Truthiness of Lists

When used as a conditional, a list evaluates to True unless it is empty.
This can be very convenient when writing conditional expressions involving lists.

```python
my_wallet = [10, 10, 20, 1, 1]
if my_wallet:
    print("I have some money!")
```

> An annotation points out that the Non-empty list in `my_wallet` evaluates to `True`, so the print statement will be executed.

#### Printing Lists

When you print a list, you will notice that the square brackets are printed too.
In fact, Python print each value of the list as if it was a literal value.
So notice that the strings have quotes around them now!

```python
>>> names = ["Alice", "Bob", "Carol"]
>>> print(names)
['Alice', 'Bob', 'Carol']
```

#### The Box Model
Lists are often shown in diagrams as a row of boxes, to help us visualize the data.
Each box will have a value in it.

> On the left is a list literal value:

```python
[10, 10, 20, 1, 1]
```

> On the right, the same values are shown in adjacent boxes.

| 10 | 10 | 20 | 1 | 1 |
|----|----|----|---|---|

#### List Type

When you define a function, you need to specify the types of the parameters and the return value.
If you don't know the element type of the list, you can just use the `list` type like we would a string or an integer.
The left function consumes a list and produces an integer.
But if we do know the element type, we wrap the type expression in square brackets.
The right function consumes a list of integers and produces a list of strings.
There are other ways to specify a list type, but this will be sufficient for our purposes.

> A function that consumes a list and produces an integer:

```python
def transform_list(some_list: list) -> int:
    pass
```

> A function that consumes a list of integers and produces a list of strings:

```python
def ints_to_strs(numbers: [int]) -> [str]:
    pass
```

#### Terminology
Some people will use the words "Array" or "Vector" to describe lists.
These are actually slightly different concepts, which we will not cover in this course.
Don't be thrown off if someone refers to a list as an "Array", but don't use that word yourself!

> The term "List" is different from the terms "Array" or "Vector".

