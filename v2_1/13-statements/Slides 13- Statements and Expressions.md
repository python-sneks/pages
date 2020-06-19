# &icon-ms-ppt; Slides

[Download slides](https://udel.instructure.com/files/74607484/download){: .instructure_file_link .instructure_scribd_file }

# &icon-video; Video

<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/Gv9dP4RgccM?feature=oembed&amp;rel=0" 
></iframe>

# &icon-document; Transcript

#### Sequence

Programs execute line by line, one step at a time.
Many times, the programs run super fast, and you won't see this behavior. 
We have some tools that let us slow down and see the execution.
But either way, programs run one line at a time.

> The following program, with an arrow on the left pointing down along the line numbers (1, 2, etc.):
```python
count = 0
print(count)
count = count + 5
count = count + 2
print(count)
```

#### Metaphor

Think about reading a book or acting out a script, how we move down a page.
This is just like how the instructions of a program are read.

> A person reading a book, with an arrow pointing down the page.

#### Time

The result of this step-by-step instruction is that programs are executed *over time*.
Although execution happens very, very fast, it does not happen all at once.
Time is a crucial component in running programs.

> The program from before, with a picture of a clock on the left. Below the program, there is the following text:
    Line 1 took 1 millisecond
    Line 2 took 3 milliseconds
    Line 3 took 2 milliseconds
    Line 4 took 2 millliseconds
    Line 5 took 3 millliseconds
    Total execution time: 11 milliseconds

#### Statements

A single line of code is known as a "Statement".
A program is really a collection of statements.
There are many kinds of statements, but we only know about a few so far.

> An "Assignment Statement" is shown and labeled as such:
```python
count =
```
> A "Print Statement" is shown and labeled as such:
```
print(count)
```

#### Expressions

An expression is any kind of combination of literal values, arithematic operators, boolean operators, and variables.
Any value is an expression.
Any variable is an expression.
Expressions can be made up of expressions.

> A series of expressions labeled as Literal Values: `5`, `10.0`, `True`, `"Hello"`, `None`  
> A series of expressions labeled as Arithmetic operators: `1 + 2`, `4 - 5`, `8 / 4`  
> A series of expressions labeled as Boolean operators: `5 > 4`, `False or not True`  
> A series of expressions labeled as Variable: `age`, `score`, `my_string_variable`
> One more expression annotated as Expressions inside of Expressions inside of Expressions: `(1 + 5) > age and not True`

#### Connecting Statements and Expressions

In BlockPy, you can see that expression blocks have a rounded left edge.
Statement blocks have a pointy bit on the bottom and a notch on the top.
This visually shows you the difference between statements and expressions.

> On the left, a picture of BlockPy statement blocks highlighting that they have vertical notches (an assignment block and a print block).  
> On the right, a picture of BlockPy expression blocks highlighting that they have only a rounded connecting edge on the left (an addition block, a string value block, and a number value block).

#### Order is Important

Since programs run from top to bottom, the order of statements is important.
If you rearranged the sentences of a book at random, they wouldn't make much sense - the same is true for  programs.

> A picture of a confused person looking at a series of book chapters out of order: "Chapter 15", "Chapter 1", "Prologue", "Chapter 5".

#### Evaluation

We say that the computer "Evaluates" an expression, when it reduces it.
The "evaluation" doesn't happen until the program is run.
It is important to learn how to "evaluate" expressions in your head.

> On the left, the following code is shown:
```python
print((5 + 3) * 4 > 8)
```
> On the right, the subtitle "In the computer's head" is shown above the following lines:
    First, `5+3` is replaced with `8`
    Next, `8*4` is replaced with `32`
    Then, `32>8` is replaced with `True`
    Lastly, `True` is printed to the console


#### Order within Expressions

Following the order within expressions is tricky, because they are not always left to right.
Consider this mathematical expression, where the addition happens before the multiplication.
The same thing happens with an assignment; the expression on the right is evaluated BEFORE the assignment occurs on the left.

> On the left, the subtitle "Math" is above the expression `5 * (4 + 2)`  
> An annotation points out that `4+2` is evaluated to `6` and then `5*6` is evaluated to `30`.  
> On the right, the subtitle "Assignment" is above the following code:
```python
score = 5 + 3
```
> An annotation points out that `5+3` is evaluated to `8`, then `5` is stored in `assignment`.
