
[Download slides](https://udel.instructure.com/files/78929711/download){: .instructure_file_link .instructure_scribd_file }


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/cx686txSx_c?feature=oembed&amp;rel=0" 
></iframe>


#### Doing Things Multiple Times

Observe the code below, which prints out the following 5 numbers.
We had to write a print statement 5 times, once for each number.
Surely there's a way that will let us stop writing the same chunk of code each time?
For Loops are an amazingly useful tool that let us perform an action on each element of a list.

> Given the code:

```python
costs = [100, 25, 25, 50, 10]
```

> Then the following code...

```python
print(costs[0])
print(costs[1])
print(costs[2])
print(costs[3])
print(costs[4])
```

> ... can be translated into

```python
for a_cost in costs:
    print(a_cost)
```

#### For Loop Syntax

Here's how we write a For loop.
First, we write the word `for`.
Then we make a new variable named the iteration variable.
We'll come back to this later.
Next, we write the word `in`.
Then, we put the list variable or value that we want to iterate over.
After that, we need to put a colon (`:`).
Finally, we put statements inside the body of the loop, indented with 4 spaces.

```python
for item in a_list:
    pass
```

> Annotations point out each part of the loop definition.

#### The Iteration List

A crucial element of any For loop is the iteration list.
This is the data that we want to iterate over.
When the loop executes, each item of the list will be assigned to the iteration variable in turn.
It doesn't matter if the list has no items, ten items, or a thousand items; Python will still process each one in turn.

> An arrow points from `a_list` to `item` in the following code:

```python
for item in a_list:
    pass
```

> Annotations point out that each element in turn is assigned to the iteration variable.  
> Additionally, the following table is shown to highlight the values inside of `a_list`:

| 10 | 10 | 20 | 1 | 1 |
|----|----|----|---|---|

#### The Iteration Variable

One of the hardest things to understand about For loops is the iteration variable.
The iteration variable represents the generalized version of each item in the list.
If you have a list of temperatures, it is "a temperature".
If you have a list of books, it is "a book".
By performing operations on this generalized version of a list item, you can work on the entire list while only having to think about one element at a time.
The iteration variable is created by the For loop when it executes.
The type of the iteration variable is the same type as the element type of the list.

```python
for a_temperature in temperatures:
    pass

for a_book in books:
    pass

for a_name in names:
    pass

for a_fruit in fruits:
    pass
```

#### The Body

Just like an If statement, we can put statements inside of a For loop.
Each statement is indented with four spaces, and each statement will be executed one-by-one, from top to bottom.

```python
for a_price in prices:
    adjusted = a_price * .9
    print(adjusted)
```

> An arrow points from the first line down to the third line.

#### The Flow of a For Loop

Previously, we said that a program was like a river, running from the top to the bottom.
If statements made the stream split into two directions.
For loops also make the stream split, but one of the new streams will move back up.
This is the crucial idea, and its why we call it a loop.
The program will LOOP until each element of the list has been assigned to the iteration variable.

```python
for a_price in prices:
    adjusted = a_price * .9
    print(adjusted)
```

> An arrow points from the first line down to the third line and then curves back up (forming a loop).

#### The Scope of a For Loop

Unlike functions, For loops do not have their own scope.
Variables defined outside of a For loop can be used inside the loop body.
The iteration variable can be used after the loop has finished.
Nothing special has to be done with regards to scope with loops.

> The following code is shown:

```python
numbers = [1, 5, 2]
message = "The number is"
for number in numbers:
    print(message, number)
print("The last number was", number)
```

> Annotations point out that all three variables are available inside the loop, and after the loop is finished.

#### Tracing a For Loop
Let's look at a loop in practice.
Notice how the value of the iteration variable changes each time we go through the loop again, and the cursor jumps back up to the start of the loop.
This behavior is crucial!


> A visualization is shown, available at: https://goo.gl/yebYBw

