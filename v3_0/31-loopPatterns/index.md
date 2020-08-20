# Loop Patterns

[Download slides](Loop%20Patterns.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/RaO83VGx9GY?feature=oembed&amp;rel=0" ></iframe>


#### Many Patterns
There are so many ways to use For loops.
In this lesson, we will review a few common patterns.
These patterns shown here are just starting points.
Think of them as templates that can be adapted and combined to solve more complex problems.

* Count
* Sum
* Accumulate
* Map
* Filter

#### The Count Pattern
We have a list of items, and want to know how many there are.
A simple algorithm is, starting with an initial value of 0, to add 1 for each element we see to a "count" variable.
When the loop is finished, the "count" variable will have the length of the list.

> The variable `count` is called the "Accumulator variable"

```python
count = 0
for item in a_list:
    count = count + 1
```

#### The Sum Pattern
We have a list of numbers, and want to add them all up.
The plus operator can only take two items at a time, however.
Therefore, we add each element one at a time to a "sum" variable, which is also initialized to 0.
As you can see the, the sum pattern is similar to the Count pattern, except instead of adding 1, we are adding the iteration variable.

> The variable `sum` is called the "Accumulator variable"  
> The variable `item` is called the "Iteration variable"

```python
sum = 0
for item in a_list:
    sum = sum + item
```

#### Accumulator Pattern
The Sum and Count patterns are both more specific examples of the accumulator pattern.
In general, this pattern allows us to start with an initial value and use any function or operation that takes in two values.
This pattern can be applied to numbers, but it also works for strings, booleans, and even lists.
This process of accumulation is also sometimes known as "reducing" or "folding" a list.

> General Template:

```python
result = ___
for item in a_list:
    result = result ___ item
```

> Strings (join together):

```python
result = ""
for item in a_list:
    result = result + item
```

> Booleans (any true?):

```python
result = False
for item in a_list:
    result = result or item
```

> Booleans (all true?):

```python
result = True
for item in a_list:
    result = result and item
```

#### The Map Pattern
What happens when we accumulate a list?
If we start with an empty list as our initial value, and append each value one at a time, we end up with a copy of the original list.
As we're appending values, we can also modify them.
For example, you could double each value from the old list, or convert each temperature from Fahrenheit to Celsius.

```python
copied_list = []
for item in old_list:
    copied_list.append(___)
```

> You can replace the blank with an expression involving `item` such as `item * 2`

#### The Filter Pattern

We have a list of numbers, and want to ignore some of them according to a rule.
By embedding an IF statement inside the loop, we can optionally include or not include elements in our accumulation.
The Filter pattern is very compatible with the other patterns.

> The following code is an example of the `Map + Filter` pattern.

```python
new_list = []
for item in a_list:
    if item < 100:
        new_list.append(item)
```

> The following code is an example of the `Count + Filter` pattern.

```python
result = 0
for item in a_list:
    if item < 100:
        result = result + 1
```

#### Inside or Outside of the Body
Novices struggle with what goes inside or outside of a loop body.
Remember, every statement inside the body is executed for each element.
Only put things inside if they should happen for each element.
The patterns can help you keep track of where things go, but ultimately you have to think critically to know.

```python
# Before
for item in a_list:
    # Inside
    pass
# After
```
