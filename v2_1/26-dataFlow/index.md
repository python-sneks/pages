
[Download slides](Data%20Flow.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/SZ96CAwNPgg?feature=oembed&amp;rel=0" 
></iframe>




#### Scope and Values

Previously, we learned about scope: the idea that variables inside a function cannot be used outside of the function, and variables outside a function should not be used inside the function.
Further, we learned that functions do not consume or return variables; instead they consume and return values.
These ideas are critical in understanding how data flows through a program.

1. Variables inside a function cannot be used outside
2. Variables outside a function should not be used inside
3. Function return values, not variables

#### Data Flow

You can think of a program as a flowing, twisting river.
Regular execution makes the river flow south, but functions disrupt this flow.
Along the way, values are carried by the current.
At times, we give these values names by using variables, but it is the values that flow through the program, not the variables.

> A picture of a winding river, with values (e.g., `64` and `"Klaus"`) inside. Some of the values are annotated with the names of variables.

#### Substitution

When you call a function, each parameter is assigned the value of a relevant argument. 
When you return from a function, the function call is substituted for the returned value.
These are the only tools we should use in Python to move data around a program.

```python
def make_fraction(top, bottom):
    return top/bottom

ratio = make_fraction(6, 3)
```

> Annotations point out that `top` and `bottom` are new variables and will have the values `6` and `3` respectively.  
> The expression `make_fraction(6, 3)` will be substituted for `2.0`.

#### Data between Functions

To move data from one function to another, you cannot just look at the two functions.
You must also look at where the functions were called.
The returned value of one function should be fed into the next function.

```python
def calculate_grade(raw, weight):
    grade = 10 * (weight+raw) ** .5
    return grade
    
def print_grade(grade):
    print("Your grade was:", grade)
    
raw = 45
weight = 5
grade = calculate_grade(raw, weight)
print_grade(grade)
```

> Annotations point out that the variables defined inside `calculate_grade` are distinct from the variables outside of the function.  
> Another set of annotations point out that the last 4 lines are the ones that actually move values between functions.