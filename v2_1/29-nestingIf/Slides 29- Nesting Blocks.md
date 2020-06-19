# &icon-ms-ppt; Slides

[Download slides](https://udel.instructure.com/files/75278286/download){: .instructure_file_link .instructure_scribd_file }

# &icon-video; Video

<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/4TCAozC9P_A?feature=oembed&amp;rel=0" 
></iframe>

# &icon-document; Transcript


#### Nesting
You can put IF statements inside of IF statements.
We call this "nesting".
As you develop more complex programs, you will do a lot of nesting.

```python
if age > 21:
    if cost < 10:
        print("Buy")
    else:
        print("Too expensive")
else:
    print("Too young")
```

> An annotation points out that the second `if` statement is a "Nested Inner `if`".

#### Number of Spaces

Whitespace rules can be confusing.
Every time you nest a block inside another block, the body gets indented another 4 spaces.
Observe the BlockPy blocks on the left, and their resulting whitespace on the right.

> On the left, an block representation of a program is shown.  
> On the right, the comparable Python code is shown:

```python
if age > 21:
    if cost < 10:
        print("Buy")
    else:
        print("Too expensive")
else:
    print("Too young")
```

> Annotations point out that there are 4 spaces on the second, fourth, and last lines.  
> More annotations point out that there are 8 spaces on the third and fifth lines.

#### IF and Functions

You can put IF statements inside of functions.
In fact, this is both common and useful.
Remember the whitespace rules when this occurs.
Each nested block is another 4 spaces in.

> On the left, an block representation of a program is shown.  
> On the right, the comparable Python code is shown:

```python
def adjust_price(price, age):
    if age > 60:
        return price * .8
    else:
        return price
```

> Annotations point out that there are 4 spaces on the second and fourth lines.  
> More annotations point out that there are 8 spaces on the third and fifth lines.

#### What Goes Inside?

It can be difficult to know if something belongs inside or outside of a block.
You must be aware of what you are trying to do with the IF block.
Remember: statements inside the IF block are executed only if the conditional evaluates to True.
Think critically!

> On the left side, there is annotation ("Third line is always executed") and the code:

```python
if cost > 5:
    discount = 10
price = 10
```

> On the right side, there is an annotation ("Third line is SOMETIMES executed") and the code:

```python
if cost > 5:
    discount = 10
    price = 10
```

#### ELIF block

In addition to the IF and ELSE blocks, there is a third type: ELIF.
The ELIF is exactly equivalent to an ELSE block with an IF inside.
However, they are sometimes used for convenience.

> On the left, there is the following code:

```python
if "dog" in name:
    print("Is a dog")
else:
    if "cat" in name:
        print("Is a cat")
    else:
        print("Unknown animal")
```

> On the right, there is code meant to be seen as equivalent:

```python
if "dog" in name:
    print("Is a dog")
elif "cat" in name:
    print("Is a cat")
else:
    print("Unknown animal")
```

> An annotation points out the use of the `elif` keyword.

#### Two IFs vs ELSE IF

The following two pieces of code may look similar, but they are quite different.
The code on the left has two IF statements, and both will always be evaluated and potentially executed.
The code on the right has an ELIF statement, and the second will only be evaluated if the first one evaluates to false.

> The code on the left has an annotation that points out that if the `name` is `"catdog"`, both lines get printed.

```python
if "dog" in name:
    print("Is a dog")
if "cat" in name:
    print("Is a cat")
```

> The code on the right has an annotation that points out that if the `name` is `"catdog"`, only the first line is printed.

```python
if "dog" in name:
    print("Is a dog")
elif "cat" in name:
    print("Is a cat")
```

#### Unnecessary IF

Two kinds of mistakes are very common with IF statements.
The first common mistake is using an IF statement when a conditional expression is fine on its own.
For example, consider this function definition that returns True if the parameter is greater than 5, or otherwise returns False.
The conditional expression already evaluates to either True or False, so it was unnecessary to use an If statement.
Instead, you can directly return the result of the conditional expression, as shown on the right.

```python
def adjust_price(age):
    if age > 60:
        return True
    else:
        return False
```

> The code above can be reduced to:

```python
def adjust_price(age):
    return age > 60
```

#### Unnecessary Test

A second common mistake is to test if a Boolean expression is equal to True.
Although the expression here, `age > 5 == True`, reads like it makes sense in English, it is redundant in Python.
`age > 5` already evaluates to either `True` or `False`.
If you compare a Boolean value to `True`, then the result is the same Boolean value.
Nothing is accomplished, you have simply made your code more complex.

```python
def adjust_price(age):
    return (age > 5) == True
```

> The code above can be reduced to:

```python
def adjust_price(age):
    return age > 5
```
