
[Download slides](https://udel.instructure.com/files/78525822/download){: .instructure_file_link .instructure_scribd_file }


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/BX7o3ueHaGA?feature=oembed&amp;rel=0" 
></iframe>


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
You write `def`, the name of the function, an open parentheses, each of the parameters separated by commas, a closed parentheses, a dash, a greater than, the return type of the function, and a colon.
The parameters need their variable names, a colon, and their parameter type.
This entire line is called the header.

```python
def name(p1: int, p2: str) -> bool:
```

> Annotations mark each part of the function definition.
> `def` is the define keyword
> `name` is the name of the function
> `(` and `)` are the parentheses
> `p1` and `p2` are parameters' names
> `int` and `str` are the parameters' types
> `,` is a comma, separating the parameters
> `->` is dash and a greater than, forming an arrow
> `bool` is the return type
> `:` is a colon, ending the header

    
#### Function Body
When you call a function, you are executing the code stored in the "Body" of the function.
Everything "inside" the body should be indented 4 spaces.
In the block version, this is shown visually with the bar on the left.
The body can be one or more lines long - in other words, it cannot be empty.

```python
def a_function(something: int) -> bool:
    modified = something * 5
    is_big = modified > 10
    return is_big
```

> An annotation points out that the body of the function is indented 4 spaces.  
> On the right, the same code is shown as blocks, with a highlight around the left side of the block (representing the indentation).

#### Pass
Sometimes, we want to define a function without writing its body just yet.
We use a special statement named "pass" to fill in the body until we're ready to write it.
Pass is a very special statement: it does absolutely nothing but take up space.

```python
def func(abc: bool) -> str:
    pass
```

> An annotation explains that the `pass` statement means "do nothing".

#### Tricky Colons
A number of statements in Python require colons at the end.
Functions require colons at the end of the header.
One of the most common mistakes people will make is to forget the colon.

```python
def name() -> None:
    pass
```

> An annotation is pointing to the colon and reads "Seriously, don't forget the colon."

#### Naming a function
Naming a function is just like naming a variable.
The same rules even apply: you may only use letters, numbers, and underscores, and it cannot start with a number.
Choose the name of the function based on what it does at a high level - typically it should be a verb.

1. Names can only have
    * Letters
    * Numbers
    * Underscores (\_)

2. Names must begin with
    * A letter
    * An underscore (\_)
    
#### Calling Your Functions

After you've defined a function, you can use it.
Again, we combine the name of the function with parentheses.

```python
def print_name(name: str):
    print("Hello", name)

print_name("Cory")
print_name("Klaus")
print_name("Ellie")
```


#### Parameters
When you define a function, you can choose to add in parameters.
These parameters will take on the value of the arguments when the function is called.
This can be very tricky to understand.

```python
def add5(a_number: int):
    new = a_number + 5

add5(10)
```

#### Parameters and Values
Remember, variables are passed into a function call as values.
When you manipulate the value of the parameter, you are NOT changing the original variable.
That means that the code below prints "5" instead of "0".

```python
def reset(a_var: int):
    a_var = 0

my_num = 5
reset(my_num)
print(my_num)
```

> An annotation points out that the second line modifies `a_var`, but not `my_num`  
> A second annotation points out that the `print(my_num)` prints 5, not 0.

#### Parameters and Types

In modern Python, we can optionally specify the type of each parameter.
So far, we know of five types: int, str, float, bool, and None.
Any time you call that function, the arguments must match the type of the parameter.

```python
def area(length:int, width:int) -> int:
    return length * width


area(4, 5)
```

> Annotations on the code point out the parameter types (both are `int`)
> Another annotation points to the function call at the bottom, and says that the arguments must match the parameter types.

#### Return
When defining a function, you can make it return a value.
Most functions return some kind of value. 
We make Python return values using the "return" statement.
We can also specify the type of value that the function returns using the arrow and a type in the header.

```python
def area(length:int, width:int)->int:
    return length * width
```

> An annotation points out that the second line is a `return` statement.
> Another annotation points out the arrow (`->`) and return type (`int`)

#### The Effect of Returning

When your function returns something, the calling block will change its shape.
This connects to the earlier ideas about expressions and statements.
When it comes to functions, returning values make functions behave as expressions instead of statements.

> On the left and right there are BlockPy blocks of code, each side having a function definition and a function call.  
> The first function has a return statement, which makes the first call have a notch on its left side.  
> The second function does not return, which makes the second call have a flat left side but notches on the top and bottom.

#### Returns Go in Functions

Return statements can only be placed INSIDE of a function definition.
It is impossible to have a return outside of a function.
Any attempt to do so will give you an error message.

> A message that says "Do not put return statements OUTSIDE of a function body!"

#### Print vs. Returning

Printing and returning are two *very* different things, although that may seem confusing. 
Printing is how we write stuff to the console, while returning is used to get data out of functions.
When you return a value, you might store it in a variable and use it later or as part of an expression.
The print function does not return anything - instead it returns the special value None.

> Two sets of code, one on the left and one on the right.  
> On the left, above an annotation that reads "Prints 6":

```python
def double(a_number:int) ->int:
    return a_number * 2

doubled = double(3)
print(doubled)
```

> On the right:

```python
def double(a_number:int):
    print(a_number * 2)

doubled = double(3)
print(doubled)
```

> An annotation points out that the second bit of code prints:

```
6
None
```

> Note the `None` being printed!