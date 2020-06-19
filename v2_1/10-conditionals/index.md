
[Download slides](Conditionals.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/8dodBDysmk4?feature=oembed&amp;rel=0" 
></iframe>


#### Purpose

One of the major reasons that programs are useful is because they can do different things depending on their inputs.
To be able to make these decisions, we need to be able to write "conditional expressions".
Think of these as a question.

> A picture of a computer with a thought bubble containing a "?".

#### Comparison Operators

Often, we want to know about the relationship between two numbers.
For this, we use the comparison operators.
Each of these operators takes two numbers and returns either True or False.

> On the left, a series of six conditional operators: `==`, `!=`, `<`, `<=`, `>`, `>=`  
> On the right, the two boolean values `True` and `False` with an arrow pointing from the operators to the values.

#### == (Equal Operator)

Okay, this is gonna sound weird, but in Python we use two equal signs to test for equality.
Do not use one equal sign, that means something different.

> A series of expressions demonstrating the equality comparison:
```python
> 5 == 5
True
> 10 == 7
False
```
> An annotation points out that you need TWO equal signs, not one.

#### != (Not equal operator)

This will be even weirder.
In Python, to test if two things are NOT equal, we use an exclamation mark and an equal sign.

> A series of expressions demonstrating the inequality comparison:
```python
> 5 != 5
False
> 10 == 7
True
```

#### <, <=, >, >= (Greater than and Less than)

There are four other operators:
The less than operator, the greater than operator, the less than or equal to operator, and the greater than or equal to operator.

> A series of expressions demonstrating the equality comparison:
```python
> 5 < 10
True
> 5 <= 5
True
> 10 > 5
True
> 10 >= 10
True
```

#### Returning True or False

I said before that the operators return either True or False.
Mentally imagine the result of these operations being replaced by True or False.
If you print the value, it will literally be True or False.

> On the left, an expression is annotated with the text "This comparison becomes True in the computer's head":
```python
> 10 == 10
True
```
> On the right, a statement is annotated with the text "This prints `False` instead of `10 != 10`":
```python
> print(10 != 10)
```
    False

#### Boolean Operators

In the same way we can add and subtract numeric expressions together, we can also combine boolean expressions together.
There are three operators for this: `and`, `or`, and `not`

> On the left, a series of three boolean operators: `and`, `or`, `not`  
> On the right, the two boolean values `True` and `False` with an arrow pointing from the operators to the values.

#### And

And returns True if both the left and right expressions are True.

> On the left, a series of example operations:
```python
> 4<5 and 5<6
True

> 5<4 and 5<6
False

> 5<4 and 6<5
False
```
> On the right, a truth table demonstrates the results.

| Left | Right | Result |
|-------|-------|--------|
| False | False | False |
| True | False | False |
| False | True | False |
| True | True | True |

#### Or

Or returns True if either the left or right expressions are True.

> On the left, a series of example operations:
```python
> 4<5 or 5<6
True

> 5<4 or 5<6
True

> 5<4 or 6<5
False
```
> On the right, a truth table demonstrates the results.

| Left | Right | Result |
|-------|-------|--------|
| False | False | False |
| True | False | True |
| False | True | True |
| True | True | True |

#### Not

Not returns True if the expression is False.
Unlike AND and OR, the NOT expression only takes in a single value.

> On the left, a series of example operations:
```python
> not 4<5
False

> not 5<4
True
```
> On the right, a truth table demonstrates the results.

| Value | Result |
|-------|--------|
| False | True |
| True | False |

#### Nesting Conditionals

You can connect conditionals into fairly complex expressions, just like you could with math.

> A series of expressions demonstrate how you can nest conditional operators:
```python
> (5 < 4 and 3 > 7) or (not False and 3 < 2)
False
> not (not (not (not True)))
True
```

#### Conditionals Are Not Distributive

A common beginner mistake is to think that you can distribute conditionals.
You might think that the code shown here asks if the number 5 is less than 1 or less than 2.
But the "or" operator makes the 2 evaluated separately.
To properly ask this question, you need to write the statement below, with the less than operator used a second time.

> The label "Wrong!" is applied to:
```python
5 < 1 or 2
```
> The label "Correct!" is applied to:
```python
5 < 1 or 5 < 2
```
