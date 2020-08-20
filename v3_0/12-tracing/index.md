# Tracing

[Download slides](Tracing.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/brqAB3kZ8kc?feature=oembed&amp;rel=0" ></iframe>


#### Syntax

To write to a variable, you put its name on the left side of an "assignment statement".
To read from a variable, you simply use its name.

> Left: Examples of "Writing"
```python
my_int_variable = 5
my_str_variable = "hello"
my_bool_variable = True
```
> Right: Examples of "Reading"
```python
print(my_int_variable)
new_variable = old_variable + 7
```

> An annotation points out that the second "Reading" line is also writing to `new_variable` in addition to reading from `old_variable`

#### = vs. ==

Notice that assignment statements use a single equal sign, and the equality operator uses two.

```python
new_boolean_variable = (5 == 4)
```
> The line of code is annotated to point out that the single equals (`=`) is an assignment, while the double equals (`==`) is an equality comparison.

#### Lifetime

Variables have a lifetime.
At some point in the program, they are initialized, and then later on they are used.
At any given time, you can ask what the value of a variable is, and change it.

```python
football_score = 0
football_score = 10
football_score = 27
```
> Each line of code shown is annotated to highlight that the variable `football_score` is changing value on each line (to `0`, then `10`, and finally to `27`).

#### Read after Write

A variable cannot be read until it has been written.
If you attempt to read an unwritten variable, an error will occur.

> On the left, the subtitle "Good" is above two lines of code:
```python
age = 5
print(age)
```

> On the right, the subtitle "Bad" is above two lines of code:
```python
print(age)
age = 5
```
> The code on the right is shown with an annotation demonstrating the specific error message that will occur:

    Traceback (most recent call last):
      File "<stdin>", line 1
    NameError: name 'age' is not defined


#### Update

We often want to increase or decrease a variable by a variable.
For instance, when we're counting the number of things in a list, we need to add one to a variable.

We could do: x = x + 1

This really highlights the difference between math and computing.
In algebra, it would have been impossible to write that statement, because you were solving for x.
But in computing, you are ASSIGNING to x.
You are overwriting whatever was there before.
That's why you should read this statement starting from the right side.
It literally means, "Take the expression on the right and replace the variable on the left with it"

> Three lines of code are shown:
```python
count = 0
count = count + 1
count = count + 1
```
> The second line is annotated with the note that "The count variable is replaced by 0"  
> The third line is annotated with the note that "The second time, the count variable is replaced by 1"

#### Tracing

It is often useful to track the value of variables over time.
We call this "tracing" a variable.
We often put these traces into a Trace Table.
Although the computer only keeps track of the latest state of the variables, we humans want to think about the entire lifetime of the variables.

> On the left, three lines of code are shown:
```python
count = 0
count = count + 5
count = count + 2
```

> On the right, a trace table is shown:

| Line | Value of `count` |
|------|------------------|
| 1 | 0 |
| 2 | 5 |
| 3 | 7 |

#### Initializing and Updating

The first time a variable is written to, we say that that variable has been "initialized" or "created".
Any time after that, writing to the variable is referred to as being "updated" or "changed".

> Three lines of code are shown:
```python
count = 0
count = count + 5
count = count + 2
```
> The first line is annotated as "Initialization", while the other two lines are annotated as "Updates"

#### Terminology

Besides "reading" and "writing", there are many other words. You should get a sense of the different ways we refer to variables.

| Write | Initialize | Update | Read |
|-------|------------|-----------|------|
| Set | Define | Change | Use |
| Store | Create | Increment | Load |
