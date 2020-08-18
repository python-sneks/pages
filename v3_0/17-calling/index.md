
[Download slides](Calling%20Functions.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/9FvjO1itBsk?feature=oembed&amp;rel=0" 
></iframe>


#### What Are Functions?
Functions are reusable chunks of code.
Once code is wrapped in a function, we can use it in other places.
First, we'll learn how to use functions.
Later, we'll learn how to make them for ourselves.

> The text reads "Functions: Resuable chunks of code"

#### Calling Functions
When you want to "use" a Function, we say that you "call" it.
Another term is "invoking" a function.

> The words "calling", "invoking", and "using" are shown.

#### Syntax

There are two essential parts to calling a function:
The name of the function, and then parentheses following the name.

> The following code is shown:

```python
apple()
orange()
```

> Annotations point out that the words `apple` and `orange` are the Names of the functions, and the `()` afterwards are parentheses.

#### Calling or Not

To call a function, you MUST add parentheses.
Otherwise, you are simply referring to the name of the function rather than executing it.
Think of it as the difference between "thinking about going to the store" as opposed to "actually physically going to the store".

> On the left, under the heading `go_to_store` there is a picture of person thinking about the phrase "I should go to the store!".  
> On the right, under the heading `go_to_store()` there is a picture of a person physically going to a store.  
> A note highlights the use of parentheses in the header on the right.

#### Functions vs. Programs

A program and a function are similar, but not quite the same.
They both have the same "Input-Process-Output" pattern.
However, functions are typically much smaller, and are meant to accomplish a single specific task.

> A diagram shows a box labelled "input" with an arrow pointing towards a bigger box labelled "processing", and another arrow pointing out that box pointing to "output". The bigger box is annotated as a "program".  
> Inside the bigger box is a series of three sets of three smaller boxes, each labelled "input -> processing -> output". These boxes are labelled as functions.  
> All together, there is a small black arrow tracing through all the boxes in order.

#### Functions vs. Methods

Methods are a special kind of function.
They are attached strongly to a value.
The way we write a method call is slightly different too, since it needs to incorporate that value.

```python
> "MAKE THIS LOWERCASE".lower()
"make this lowercase"
```

> An annotation points out that the `lower` is a method name.

#### Calling Methods
When you want to use a Method, you need the name, parentheses, AND two more pieces:
The calling value or variable and a period.
In later lessons, we'll learn more about this strange syntax.
For now, get comfortable with the difference between calling functions and methods.

```python
> "MAKE THIS LOWERCASE".lower()
"make this lowercase"
```

> An annotation points out that there is a value on the left (but it could have also been a variable) and a period in between the method name and the value.

#### Metaphor
You don't have to know *how* a function accomplishes its goal, in order to use it.
Think of it like a well-run office.
When you ask a co-worker to complete some work, you don't care how it happens, just the inputs and outputs to their process.
This separation of concerns allows you to focus on pieces of a program without worrying about the whole thing.

> On the left, a boss asks an employee to "create a report on sales".  
> In the middle, the phrase "time passes" appears.  
> On the right, the employee has returned and says "Here is the report, sir"

#### Returning Values

Functions are useful because they can return values.
Functions can return any type of value: string, boolean, integer, whatever.
Mentally, when a function is called, you can imagine the result replacing the entire function call.
In a way, this is similar to what happens when you do addition or subtraction.

```python
> "MAKE THIS LOWERCASE".lower()
"make this lowercase"
```

> An arrow connects the top line to the bottom line, highlighting that this value was returned.

#### Arguments
One of the most useful features of functions are arguments.
Arguments are values that are given to functions that affect the behavior of the function.
Arguments for a function are placed inside the parentheses, and each one is separated by a comma.
We say that these arguments are being "passed" to the function.

```python
print("First", "Second", "Third")
```
> An annotation points out that the three string values are "arguments" separated by commas (`,`).

#### Metaphor
Think of a function as a magic black box.
You cannot see inside the box to know how it works, but you do not need to.
Arguments are the knobs and dials on the outside of the box that let you control its workings.
Returned values are like a slot that dispenses the results of the function.

> A picture of a machine with two slots on top and one slot on the right side. Numbers are going into the slots on top and coming out of the slot on the right. The machine is labeled as "Magic Function Box", the slots coming in are labeled as "arguments", and the slot coming out is labeled as "returns".
