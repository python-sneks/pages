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