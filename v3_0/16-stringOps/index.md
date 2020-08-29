# String Operations

[Download slides](String%20Operations.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/xY0Ypzy3oew?feature=oembed&amp;rel=0" ></iframe>


#### Addition
Like numbers, you can add two strings together. This puts them side by side in
a single new string. This is sometimes called "Concatenation".

```python
> "Hello " + "World"
"Hello World"
```

#### Comparing Strings
You can test if two strings are equal, not equal, or even compare them using
less than and greater than. This measures which ones come first in the alphabet.

```python
> "Dog" == "Dog"
True 
> "Dog" != "Cat"
True
> "Aardvark" < "Zoo"
True
> "Orange" <= "Apple"
False
```

#### Membership in Strings

There's another test you can check with Strings: using the "in" operator.
This simply checks whether the first string appears in the second.
You can also use the "not in" operator to test the opposite.

```python
> "house" in "boathouse"
True
> "cow" in "cowabunga"
True
> "y" not in "axes"
True
> "xe" not in "axes"
False
```

#### Subscripting
Subscripting is one of the more powerful and more complex features of strings.
When we *subscript* a string, we extract one or more characters from the string.

```python
> "Hello world"[0]
"H"
```

#### Subscript Syntax
We can subscript a string value or variable by using square brackets.
Notice the key components: On the left is the name of the variable or the string literal value.
Next we have an opening square bracket.
Then, we have a number, which is called the index.
Finally, we end with a closing square bracket.

```python
> "Harry Potter"[1]
'a'
> book_title = "Harry Potter"
> book_title[2]
'r'
```

#### Starting at 0
Here's a weird thing: computers start counting at 0, not 1.
So if you want the first character from the string, you need to write 0 instead of 1.
There are boring math reasons why this happens, but ultimately it ends up being more convenient, once you get used to it.

> The string "Harry Potter" is written with numbers below each character.  
> The first character "H" has a zero below it, the second character "a" has a 1, etc.

#### Subscripting Multiple Characters

It wouldn't be too useful to only grab out one character at a time.
So you can actually grab out more than one by using the subscript range syntax:
Inside the square brackets, you put a pair of numbers separated by the colon.

```python
> "Hello world"[1:5]
"ello"
```
> Speech bubbles point out that the 1 is the "starting index", the 5 is the "ending index", and there is a colon (:) in between the 1 and the 5.

#### Negative Subscript Indices

If you use negative numbers as subscript indexes, you can work from the back of the list.
If you use -1, then you get the last character.
You can combine positive and negative in range.
To go from the start or the end, simply leave the number missing.

```python
> "hamster"[-1]
"r"
> "hamster"[1:-1]
"amste"
> "hamster"[-3:]
"ter"
> "hamster"[:3]
"ham"
```
