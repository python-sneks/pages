
[Download slides](Types.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Types.pdf"
src="https://www.youtube.com/embed/VZrudniujb4?feature=oembed&amp;rel=0" 
></iframe>


#### The Basic Types

All values in Python have a type.
The five basic types are: integer, float, string, booleans, and None.
There are many other types you will learn about.

> On the left, a series of five values are shown. On the right, the types of the values are shown. Arrows point between each value and type.  
> `143` -> Integer  
> `44.07` -> Float  
> `"A string"` -> String  
> `True` -> Boolean  
> `None` -> None

#### What are Types

Types control what you can and cannot do with things.
We know that a number is a number because we can add it to another number, or subtract it, or multiply it.
We can add two strings together, but we cannot subtract them - this is one reason why a string and a number are different.

> On the left, the subtitle "Good" is above 4 valid Python expressions:  

```python
1 + 2
1 - 2
1 * 2
"Adding strings " + "is great"
```

> On the right, the subtitle "Bad" is above an invalid Python expression:

```python
"Can't subtract" - "strings"
```

#### Integer Types

Integer types are whole numbers.
They include both negative and positive numbers, so there are a lot of them.
Integer is often shortened to "int" for convenience.

> The word `int` is in big letters, followed by a series of examples of integers:

```python
-1024
-55
0
1
13
1737
```

#### Float Types

When numbers have decimals, we call them Float types.
The decimal is what distinguishes Floats and Integers.
Remember - if a number has a period in it, then it is a float!

> The word `float` is in big letters, followed by a series of examples of floats:

```python
-56.4
-1.0
.0
0.5
1.02
100.
```

#### String Types

Textual data is represented using String values.
The tricky thing about Strings is that *anything* can be stored as a String.
The only thing that makes it a string is the quotes.
A special case is the "empty string", which is a pair of quotes with nothing inside.
String is often shorted to "str" for convience.

> The word `str` is in big letters, followed by a series of examples of strings:

```python
"My name is Anna"
""
"Doggo"
"5"
"Four Score and Seven Years ago..."
```

#### Boolean Types

Surprisingly often in programming, we are faced with "yes or no" values; these are referred to as Boolean values.
Specifically, we have a `True` and a `False` value.
Note that the T and F are capitailized, and there are no quotes around the words. 
Boolean is often shortened to "bool" for convenience.

> The word `bool` is in big letters, followed by the two types of booleans:

```python
True
False
```

#### The None Type

Sometimes, you need to represent the absence of value, which we call None.
The None type is a special type that has only one value.
The None type can be hard to wrap your head around, so we'll save that one for later.
For now, just remember that it has a capital N, and no quotes.

> The word `None` is in big letters, followed by the only value possible:

```python
None
```

> An annotation points out that `None` is the only value of the None type.