# &icon-ms-ppt; Slides

[Download slides](https://udel.instructure.com/files/78540229/download){: .instructure_file_link .instructure_scribd_file }

# &icon-video; Video

<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/HHWlfF8omAw?feature=oembed&amp;rel=0" 
></iframe>

# &icon-document; Transcript


#### Returning and Printing

Printing and returning are two related but different ideas.
However, many beginners confuse them.

* Printing: Putting things on the console
* Returning: Substitute calling expression with a value

#### Metaphor

Consider these two different scenarios.
Say I ask you to recite a poem out loud.
One you are done, the poetry is no longer available to me.
I heard it, and then it was gone.
This is like printing.
Now, say I asked you to write that poem down and hand it to me.
The poem on paper is a concrete thing that I could hand off to someone else, make edits to, or even destroy.
This is like returning a value.

> On the left, a person standing delivering a poem.  
> On the right, a person handing someone a poem on a sheet of paper.

#### Printing

Variables and data stored inside of a computer are invisible to us.
In order to see the results of computation, we often print variables and values.
Calling the built-in print function will cause text to appear on the console.
Printing data to the console is a one-way trip, and we cannot get data written there back.

> In the code below, an arrow points from the 3rd line (`print(curved)`) to a box labelled "Console" that has the text "44.0" inside of it.
```python
def calculate_grade(grade:int, weight:int)->float:
    curved = 100 * grade ** .5 
    print(curved)
    final = curved * weight
    return final
```

#### Returning

When a function is called, execution jumps to somewhere else in the program.
Some computations occur, and sometimes a result emerges.
When we want to use this result in the calling location, we need to return it.
When we use the return statement, execution jumps back to where the function was called.
The value returned is substituted in place of the function call.

> An animation is shown, demonstrating the order of the lines executed. Given the following code:

```python
def calculate_grade(grade:int, weight: float)->float:   # 1
    curved = 10 * grade ** .5                           # 2
    print(curved)                                       # 3
    final = curved * weight                             # 4
    return final                                        # 5

calculate_grade(64, .1)                                 # 6
```

> Arrows indicate the order of execution: lines 1, 6, 2, 3, 4, 5, 6  
> Note that the first line is executed, followed by the line AFTER the function's definition, which then jumps back up to the start of the function's body.

#### Syntax

Let's look at the syntactic differences between printing and returning.
Return is a special keyword statement.
Print is a built-in function.
This is why print needs parentheses and return does not.
Code inside of a function can print, return, or both.
But code outside of a function can print, but it cannot return.

> On the left, the word "Printing" is above the following code:

```python
print("Hello World")
```

> On the right, the word "Returning" is above the following code:

```
return "A value"
```

> Annotations point out that printing requires parentheses but return does not.

#### When to Return

When someone tells you to write a function to produce a certain value, you will need to return.
The return needs to be the last thing that the function does, because you can only return from a function once.
You only ever return inside functions, to the place where the function was called.
In general, we return data when another part of the program needs that information.

> The slide reads: Write a function that consumes a string and **produces** that string backwards.  
> An annotation points out that "returns" and "produces" mean the same thing.

#### When to Print

Sometimes, we write functions that print.
Sometimes, we are expected to print the result of calling a function.
Sometimes, we don't print at all.
You must read instructions carefully to know what you are required to do to solve a particular problem.
In general, however, we print when we need to get information to the user, as opposed to somewhere else in the program.


> The slide reads: Write a function that consumes a string and prints it out backwards  
> Lower down, another part reads: Write a function that consumes a string and produces that string backwards; then print the result of calling the function
> Annotations point out that the first part is just printing, while the latter part is calling, returning, and printing.
