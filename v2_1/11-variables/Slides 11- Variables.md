# &icon-ms-ppt; Slides

[Download slides](https://udel.instructure.com/files/74606807/download){: .instructure_file_link .instructure_scribd_file }

# &icon-video; Video

<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/X92iyr6WNEA?feature=oembed&amp;rel=0" 
></iframe>

# &icon-document; Transcript

#### Purpose

Variables let us store and load information.
In other words, we can "read" from and "write to" a variable with data.
This lets us use data later.

> The following code is shown:
```python
our_ages = [15, 27, 32, 14]
total_age = 0
for age in our_ages:
    total_age += age
print(total_age)
```
> Every occurrence of `our_ages`, `total_age`, and `age` are circled in red and labeled as "Variables".

#### Metaphor

You can think of a variable as a box that holds data.
That data could be a number, a string, or any type of data.
After the data is put in, we can take it out later.

> The number `88` has an arrow coming out of it, pointing towards a box labeled `total_age`, with another arrow coming out of the box.

#### Variables vs. Data

Anywhere that you use literal data, you can replace it with a variable.

> On the left, the following code is shown:
```python
print(14)
```

> On the right, the following code is shown:
```python
age = 14
print(age)
```

> Annotations of the code on the right side indicate that the first line is a "Write" of `age` and the second line is a "Read" of `age`.

#### Different from Math

Variables in computing are very different from variables in math.
In math, a variable is an unknown that we are solving for.
In computing, we always know the value of a variable, but we are manipulating it.
A variable varies over time, but according to instructions that the programmer has written.

> On the left, the subtitle "Math (Algebra)" is shown with a red X:
    y = 5 * x + 3
    y = 5 * (1 + y) + 3
    y = 5 + 5*y + 3
    y - 5*y = 8
    - 4 * y = 8
    y = -2
> On the right, the subtitle "Computing" is shown with a green checkmark:
```python
football_score = 0
print(football_score)
football_score = 10
print(football_score)
football_score = 27
print(football_score)
```

#### Names

Variables are defined by their name.
Names are absolutely crucial in programming, and choosing them is an art.
Names are best when they are accurate, meaningful, and concise.
We use good variable names to communicate clearly; not just with other programmers, but with ourselves as we try to figure out code that we have written.
Of course, computers do not understand variable names

> Two people are looking at the following line of code:
```python
temperature = 20
```
> The first person is thinking the variable represents the temperature in Celsius. The second person is thinking the variable represents the temperature in Fahrenheit.

#### Naming Rules

There are two rules for naming variables:
Names can only have letters, numbers, and underscores (_).
Names must begin with a letter or underscore

> The name rules above are written out.
