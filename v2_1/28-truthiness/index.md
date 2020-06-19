
[Download slides](Truthiness.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/2Nr1ZDbGtI8?feature=oembed&amp;rel=0" 
></iframe>


#### Truthiness

Unlike some languages, Python does not require that IF statements have boolean expressions in their conditional.
This may seem surprising, but it is actually an extremely convenient feature named Truthiness.
The idea is that any expression, whether it is an integer, string, boolean, or otherwise, can be evaluated in a conditional.

* No Booleans required!
* Or <, >, !=, ==, <=, >=, or, and, not

#### Type Truthiness

Any expression can be evaluated as a conditional according to the rules of Truthiness.
How it is evaluated depends on its type.

| Type | False | True |
|---------|-------|-----------------------------------|
| Boolean | False | True |
| Integer | 0 | Non-zero number (e.g., 5, -3) |
| Float | 0.0 | Non-zero number (e.g., -3.0, 2.4) |
| String | "" | Non-empty string (e.g., "Hello") |
| None | None |  |

#### String Example

Let's look at a simple example, where we take some input from a user.
If the user entered an empty string, then we'll print out a different message.

```python
name = input("What is your name?")
if name:
    print("Your name is", name)
else:
    print("No name given.")
```

> An annotation points out that the second line is "Truthy use of variable `name`"

#### Unnecessary Comparisons

When you need to check if a string is not empty, or a number is not 0, truthiness is the way to go.
Notice how each of the following can become much more concise and clear.

> Truthy string:

```python
if a_string != "":
    ...
# Simplifies to
if a_string:
    ...
```

> Truthy numeric:

```python
if a_number != 0:
    ...
# Simplifies to
if a_number:
    ...
```
