# Data Flow

[Download slides](Data%20Flow.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/SZ96CAwNPgg?feature=oembed&amp;rel=0"></iframe>




#### Scope and Values

Previously, we learned about scope: the idea that variables inside a function
cannot be used outside of the function, and variables outside a function
should not be used inside the function.
Further, we learned that functions do not consume or return variables;
instead they consume and return values.
These ideas are critical in understanding how data flows through a program.

1. Variables inside a function cannot be used outside
2. Variables outside a function should not be used inside
3. Function return values, not variables

#### Data Flow

You can think of a program as a flowing, twisting river.
Regular execution makes the river flow south, but functions disrupt this flow.
Along the way, values are carried by the current.
At times, we give these values names by using variables, but it is 
the values that flow through the program, not the variables.

> A picture of a winding river, with values (e.g., `64` and `"Klaus"`) inside. Some of the values are annotated with the names of variables.

#### Substitution

When you call a function, each parameter is assigned the value of a relevant argument. 
When you return from a function, the function call is substituted for the returned value.
These are the only tools we should use in Python to move data around a program.
This is just like what happens when you use an operator like plus or minus.
Even though we do not see the substitution visually, it still happens.

```python
def add(left, right):
    return left + right

5 + add(3, 4)
```

> An annotation crosses out the `add(3, 4)` and replaces it with `7`.

#### Call Frames

Each time we call a function, we say that its local variables are inside their
own scope.
We will also call this scope the **frame**, and it can be used to show
the current variables and their values.
Notice that the global frame is separate from the local frame.

```python
def add_period(text: str) -> str:
    result = text + "."
    return result

message = "Hello world"
add_period(message)
```

> There are two rectangles next to the code:
> * Frame: `add_period`
>   * `text`: str
>   * `result`: str
> * Global frame
>   * `message`: str

#### Data between Functions

To move data from one function to another, you cannot just look at the two functions.
You must also look at where the functions were called.
The returned value of one function should be fed into the next function.

```python
def calculate_grade(raw, weight):
    grade = 10 * (weight+raw) ** .5
    return grade
    
def make_grade_message(grade):
    return "Your grade was:" + str(grade)
    
raw = 45
weight = 5
grade = calculate_grade(raw, weight)
message = make_grade_message(grade)
print(message)
```

> Annotations point out that the variables defined inside `calculate_grade` are distinct from the variables outside of the function.  
> Another set of annotations point out that the last 4 lines are the ones that actually move values between functions.

#### Functions Calling Functions

Things get even more complicated when functions call other functions, but
this happens all the time.
We are used to calling built-in functions, but we can call our own functions too.
When we call a function inside another function, we **stack** the new function
 call's frame on top of the current frame, with the top frame being the current scope.
When a function call ends, we remove that top stack and return to the one below it.
Each function call's frame is separate from all other frames, even if they
come from the same function.

```python
def add5(number: int) -> int:
    result = number + 5
    return result

def double_and_add5(value: int) -> int:
    answer = 2 * add5(value)
    return answer

final = double_and_add5(7)
```

> There are three boxes on the right demonstrating the stack
> * Frame: `add5`
>   * `number`: int
>   * `result`: int
> * Frame: `double_add5`
>   * `value`: int
>   * `answer`: int
> * Global frame
>   * `final`: int
