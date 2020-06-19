# &icon-ms-ppt; Slides

[Download slides](https://udel.instructure.com/files/78540245/download){: .instructure_file_link .instructure_scribd_file }

# &icon-video; Video

<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/XUbW9qHUmnk?feature=oembed&amp;rel=0" 
></iframe>

# &icon-document; Transcript


#### Scope

In a program, the scope of a variable indicates how long that variable is available.
This is also known as the lifetime or visibility of a variable.

* "Lifetime"
* "Visibility"
* "Availability"

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
Therefore, variables defined in one function are not available outside the function.
This simplifies the reading of any function - you only need to worry about things defined in the function itself.

```python
def calculate_grade(grade:int, weight:float)->float:
    curved = 100 * grade ** .5 
    final = curved * weight
    return final

calculate_grade(90, .1)
```
> An annotation points out that, after the return statement (when the function ends), the local variables grade, weight, curved, and final are no longer available.

#### Returning Values

Functions return values, not variables.
A variable has a value, so when you write a statement like the one shown, you are returning the variable's value, not the variable itself.
The variable disappears after the function ends, so returning the value is the only way to make it available.
Any global variables with the same name are actually unrelated to the variable inside the function.

```python
def calculate_grade(grade:int, weight:float)->float:
    curved = 100 * grade ** .5 
    final = curved * weight
    return final

final = calculate_grade(90, .1)
```
> Annotations point out the following:
* There is a local variable named `final` inside of the `calculate_grade` function.
* There is a global variable named `final`.
* These two variables are unrelated even though they have the same name.

#### Global Variables Are Bad

It is technically possible to read a global variable inside a function.
However, you should not do so.
Every time you refer to global variables, your program becomes more complicated and you have to think about multiple levels of scope.
This may work out okay in smaller programs, but causes huge problems as you start writing longer programs.
Whenever you feel the urge to use a global variable, stop and reconsider.

```python
grade = 95
def print_grade():
    print("Grade:", grade)
print_grade()
```
> An annotation suggests that using the global variable `grade` inside of the `print_grade` function is bad, and that instead you should pass it in as a parameter.

#### Scope Rule of Thumb

Here is a simple pair of rules for working with scope:

* Variables inside a local scope should not be used outside that scope.
* Variables outside a local scope should not be used inside that scope.

Keeping these two rules in mind will avoid many headaches.

#### More Information

Okay, are Global Variables really bad? Let's discuss further: http://wiki.c2.com/?GlobalVariablesAreBad

