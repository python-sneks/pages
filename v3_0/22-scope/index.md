# Scope

[Download slides](Scope.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" 
        allowfullscreen="allowfullscreen" 
        webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
        title="Scope"
        src="https://www.youtube.com/embed/TuWSW80MelU?feature=oembed&amp;rel=0"></iframe>



#### Scope

In a program, the **scope** of a variable indicates how long that variable is available.
This is also known as the "lifetime" or "visibility" of a variable.

* "Lifetime"
* "Visibility"
* "Availability"

> "How long the variable is available"

#### Global Scope

Variables defined at the top level are known as global variables. 
Once a variable is defined, it is available on subsequent lines.
That variable lives until the end of the program.

```python
print("Starting program")
grade = 64
grade = grade + 5
print("Grade:", grade)
```

> An annotation points out that `grade` is available starting after line 1.

#### Local Scope

Each function has its own local scope.
Variables defined as parameters or within a function live until the function ends.
These are local variables.
Variables defined in one function's are not available outside the function.
This simplifies the reading of any function - you only need to worry about
 things defined in the function itself.

```python
def calculate_grade(grade:int, weight:float)->float:
    curved = 100 * grade ** .5 
    final = curved * weight
    return final

calculate_grade(90, .1)
```
> An annotation identifies grade, weight, curved, and final as local variables.

#### Returning Values

Functions return values, not variables.
This is so important, I'm going to say it again:
**functions return values, not variables.**
A variable has a value, so when you write a statement like the one 
shown, you are returning the variable's value, not the variable itself.
The variable disappears after the function ends, so returning the value 
is the only way to make it available.

```python
def get_grade(points:int, possible:int)->float:
    grade = points / possible
    return grade

my_grade = get_grade(70, 100)
print(my_grade)
```
> An annotation points out that the variables `points`, `possible`, and `grade`
> local variables all die after the return statement is executed.
> Another annotation points out that this prints `70.0`

#### Same Named Variables

Beginners will sometimes try to reuse a variable name 
Any global variables with the same name are actually unrelated to the 
variable inside the function.
On this slide, I have drawn squares around local variables, and circles
around global variables.

```python
def add1(number:int)->int:
    total = number + 1
    return total

total = 3
total = add1(total)
answer = 5
answer = add1(answer)
```

> Annotations point out the following:
> * There are local variables named `total` and `number` inside of the `add1` function.
> * There are global variables named `final` and `answer`.
> * These two variables named `total` are unrelated even though they have the same name.

#### Global Variables Are Bad

It is technically possible to read a global variable inside a function.
However, you should not do so.
Every time you refer to global variables, your program becomes more complicated
 and you have to think about multiple levels of scope.
In this code example shown here, the unit tests would fail if we swapped
the order of the last two lines.
This may work out okay in smaller programs, but causes huge problems as you 
start writing longer programs.
Whenever you feel the urge to use a global variable, stop and reconsider.
The only exception is if you are 100% certain that the global variable's value
will stay constant and never change.

```python
from cisc108 import assert_equal

my_title = "Lord "
def add_title(name: str) -> str:
    titled_name = my_title + name
    return titled_name

assert_equal(add_title("Bart"), "Lord Bart")
my_title = "Dr. "
assert_equal(add_title("Bart"), "Dr. Bart")
```
> An annotation points out that the code is more complicated because
> the ordering of the last two lines is more complicated.

#### Scope Rule of Thumb

Here is a simple pair of rules for working with scope:

* Variables inside a local scope should not be used outside that scope.
* Variables outside a local scope should not be used inside that scope.

Keeping these two rules in mind will avoid many headaches.
