
[Download slides](https://udel.instructure.com/files/75542505/download){: .instructure_file_link .instructure_scribd_file }


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/RwtQmRzFEqo?feature=oembed&amp;rel=0" 
></iframe>


#### Mutability

Strings and lists are similar because they are both sequences of elements.
However, a big difference between them is their Mutability.
Strings are immutable while lists are mutable.

> A pair of diverging arrows are labelled "Lists (Mutable)" and "Strings (Immutable)"

#### Immutable Strings

Say you have a string variable.
When you add another string to that variable, you need to assign the result - otherwise it is lost.
Similarly, when you call a string method, you need to assign the result - otherwise it is lost.
This is the idea of immutability - you are never changing the string, you are simply creating new ones.

```python
name = "Austin Cory Bart"

# The following line doesn't change `name`
name.lower() 

# The following line doesn't change `name`
lowered_name = name.lower() 

# Now `name` has been changed!
name = name.lower() 
```

#### Mutable Lists

Now say you have a list variable.
When you append a value to that variable, you must not assign the result back.
The append method modifies the list variable, and then returns None, so if you assign its result you overwrite the list variable.
The append call mutated the list - it changed the data inside the list without affecting the list variable.

```python
grades = [90, 65, 78]

# This adds 98 to the list
grades.append(98)

# Bad! We add 44, but then overwrite the variable
#   `grades` with None, which is returned by `.append()`
grades = grades.append(44)
```

#### Mutability and Parameters

We have seen mutability before when we learned about parameters of functions.
Let's take a look at this function `add_x` that consumes a list and a string,
and adds the string value `"X"` to the end. When the function call is over,
only the list has actually been changed. Even though we were using local
versions of each variable, the mutability of the list type meant that the
original list was changed. If we wanted to change the `name` variable, we would
have had to return the modified value and assign it back to the `name` variable.

```python
def add_x(a_list, a_str):
    a_list.append("X")
    a_str = a_str + " X"

courses = ["Biology", "Music", "Math"]
name = "Ada"
add_x(courses, name)
print(courses)
# ["Biology", "Music", "Math", "X"]
print(name)
# "Ada"
```
