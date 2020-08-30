# Defining Functions

[Download slides](Defining%20Functions.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/4Chz3UgJVD8?feature=oembed&amp;rel=0" ></iframe>



#### Defining Functions
You can create your own functions in Python.
In fact, this is one of the most powerful features of programming, the ability
to create your own functions.

> A picture of a box labelled "Homemade Functions"

#### Why Functions?
Lets' talk about two major advantages of functions:
First, they allow us to reuse code.
Second, they allow us to debug a chunk of code in isolation from the rest of the program.

1. Code Reuse
2. Easier to debug

> A stick figure under "Code Reuse" says "I need to use this multiple times! It should be a function."
> A stick figure under "Easier to debug" says "Why isn't this part working? I'll extract it into a function to test it."

#### Definition Syntax
To create a new function, you use the `def` keyword, which stands for "define".

You write `def`, the name of the function, an open parentheses
each of the **parameters** separated by commas,
a closed parentheses,
a dash and a greater than,
the **return** type of the function, and a colon
 
The parameters need: variable names, a colon, and their parameter type.
 
This entire line is called the **Header**.

```python
def name(p1: int, p2: str) -> bool:
```

> Annotations mark each part of the function definition.
> * `def` is the define keyword
> * `name` is the name of the function
> * `(` and `)` are the parentheses
> * `p1` and `p2` are parameters' names
> * `int` and `str` are the parameters' types
> * `,` is a comma, separating the parameters
> * `->` is dash and a greater than, forming an arrow
> * `bool` is the return type
> * `:` is a colon, ending the header

    
#### Function Body

When you call a function, you are executing the code stored in the "Body" of
the function. Everything "inside" the body should be indented 4 spaces.
In the block version, this is shown visually with the bar on the left.
The body must be there - in other words, it cannot be empty.

```python
def add(left: int, right: int) -> int:
    return left + right
```

> An annotation points out that the body of the function is indented 4 spaces.  
> On the right, the same code is shown as blocks, with a highlight around 
> the left side of the block (representing the indentation).

#### Naming a function

Usually, you should use a verb as the name of the function.
The name helps other programmers understand what the function does.
Naming a function is just like naming a variable: you may only use letters, 
numbers, and underscores, and it cannot start with a number.

> Rules:
> 1. Use verbs
> 2. Function names can only have
>     * Letters (abcABC)
>     * Numbers (123)
>     * Underscores (\_)
> 3. Function names must NOT begin with
>     * Numbers
    
#### Calling Your Functions

After you've defined a function, you can use it by calling the function.
As we did before, we combine the name of the function with **calling parentheses**.
Note how we still pass in **arguments**.
Here we call the function `add5` twice, first passing in the argument 10
and then the calling it again with the argument 3.

```python
def add5(a_number: int):
    return a_number + 5

add5(10)
add5(3)
```

> Annotations indicate that the calls produce the values `15` and `8`.


#### Parameters
When you define a function, you can choose to add in **parameters** to the header.
These parameters will take on the value of the arguments when the function is called.
This can be very tricky to understand.
Each argument exactly matches one parameter.
In the code below, the parameter `first` will match to 3, -2, and -10.
The parameter `second` will match to 8, 5, and 10.
Remember, each function call happens one after the other.

```python
def subtract(first: int, second: int) -> int:
    return first - second

subtract(3, 8)
subtract(-2, 5)
subtract(10, 10)
```

#### Parameters and Types

In modern Python, we specify the type of each parameter.
So far, we know of five types: int, str, float, bool, and None.
Any time you call that function, the arguments must match the type of the parameter.

```python
def get_speed(distance: int, time: int) -> float:
    return distance / time

get_speed(6, 2)
get_speed(3, 8)
```

> Annotations on the code point out the parameter types (both are `int`)
> Another annotation points to the function call at the bottom, and says that the arguments must match the parameter types.

#### Return
When defining a function, you can make it return a value.
Most functions return some kind of value. 
We make Python return values using the "return" statement.
We describe what type of value the function returns
using the arrow and a type in the header.
But note that it is the **return statement** that actually makes a value
get returned; the header just describes what should be returned.

```python
def area(length:int, width:int) -> int:
    return length * width
```

> An annotation points out that the second line is a `return` statement.
> Another annotation points out the arrow (`->`) and return type (`int`)

#### Calling and Printing

When you call a function, a value is always returned.
Even if you forget the return statement, the special value `None` will be
returned.
If you are writing code in the console, then you will see any non-`None` values
appear.
But if you are writing code in a regular editor, the value will not appear in
the console unless you use `print`.
We will sometimes print the result of calling a function, but remember
that printing is not necessary to call a function.

```python
def area(length:int, width:int) -> int:
    return length * width

print(area(3, 4))
area(1, 8)
print(area(5, 2))
```

> Two annotations point out that the output is `12` and `10`
> The middle annotation points out that the calculated `8` is not printed

#### Pass

Sometimes, we want to define a function without writing its body just yet.
We use a special statement named "pass" to fill in the body until we're ready to write it.
Pass is a very special statement: it does absolutely nothing but take up space, telling the computer to "pass over" this line.
Since we always have to have a body, if we didn't put the word pass there, Python would crash with a syntax error.

```python
def func(abc: bool) -> str:
    pass
```

> An annotation explains that the `pass` statement means "do nothing".