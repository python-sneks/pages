
[Download slides](If%20Statements.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/G9CECQpPtl0?feature=oembed&amp;rel=0" 
></iframe>



#### If Statements

If this is true, then do that.
Otherwise, don't do it.
That's the core idea of an IF statement.

> A box labeled "IF this", with two arrows coming out  
> The first arrow goes to a box labeled "THEN this"  
> The second arrow goes to a box labeled "ELSE this"

#### Purpose

If statements make code smarter.
They let you do different things in different situations.

> Three lines of text with pictures:  
> The first line reads "IF" followed by a raining cloud.  
> The second line reads "THEN bring" followed by an umbrella.  
> The third line reads "OTHERWISE do not."

#### Syntax

There are four parts to an IF statement.
First, you have the keyword "if".
Then, you have the conditional.
The conditional is followed by a colon.
Finally, you have the body of the IF statement.

> The following code is shown:

```python
if expression:
    pass
```

> Annotations point out the components as "if keyword", "conditional", "colon", "indentation", and "body".

#### Conditionals

You already learned about writing conditionals.
Conditional expressions can be variables, comparisons, or combinations using `and`, `or`, and `not`.

```python
if 4 < 5:
    ...
if age > 21:
    ...
if "cat" in animal_name:
    ...
if rent > 2000 and rooms < 2:
    ...
if not on_fire():
    ...
```

#### Body

The body of an IF statement is a sequence of one or more statements.
This body must be indented with 4 spaces.
Anything indented below the IF keyword is said to be "inside" the IF statement.
These indented statements will be executed if the conditional was evaluates to true.
Otherwise, Python will skip right over them.

```python
if income > 2000:
    tax = .8
    adjusted = income * tax
    print("Income:", adjusted)
```

> An annotation points out that the indented lines below the `if` is the *body*.

#### The "Else" block

IF statements can optionally have an Else body.
If the conditional evaluates to false, then the ELSE will be executed instead of the IF body.
The IF body will literally be skipped over as if it didn't exist .
Only one of the two bodies will be executed!

```python
if precipitation > 0:
    print("It is raining")
else:
    print("It is NOT raining")
```

> Annotations point out the `else` keyword followed by the colon on the third line.  
> The last line is identified as the *body* of the `else`.

#### Branching

Think about your program as a flowing stream.
Normally it will go from top to bottom.
An IF statement changes that flow, to optionally go around.
We call that behavior branching.
Every time you have another IF statement, you have another two branches.

```python
if precipitation > 0:
    print("It is raining")
```

> Two lines extend from the top of the program down to the bottom.  
> One of the lines goes straight down, while the other curves inward to follow the indentation.  
> These demonstrate how the program might skip over or go through the body.

#### Tracing

We have previously shown how you can make a trace table that follows the execution of an IF statement.
We now have to add an extra column to this table, to differentiate between steps and lines.
With IF statements, it is possible that a step may skip a line of code.
Even though the program shown below has 6 lines of code, it only has 4 steps!
Notice that on lines with IF statements, we still have a step, but we simply repeat the values unchanged.

```python
1| age = 25
2| if age > 60:
3|     discount = .8
4| else:
5|     discount = 1
6| price = discount * 10
```

| Step | Line | age | discount | price |
|------|------|-----|----------|-------|
| 1 | 1 | 25 | X | X |
| 2 | 2 | 25 | X | X |
| 3 | 5 | 25 | 1 | X |
| 4 | 6 | 25 | 1 | 10 |

> Note how the trace table separates Step and Line, and that not every Line is executed.
