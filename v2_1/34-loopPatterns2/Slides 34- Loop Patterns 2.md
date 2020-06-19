
[Download slides](https://udel.instructure.com/files/78929705/download){: .instructure_file_link .instructure_scribd_file }


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/9FOZ6t04ZAs?feature=oembed&amp;rel=0" 
></iframe>


#### More Patterns

We've already seen the Accumulate, Map, and Filter patterns.
Now we're going to cover a few more patterns that have more complex conditionals.

* Find
* Take
* Min/Max

#### The Find Pattern

We have a list of items and want to find a specific value based on a condition.
This requires us to walk through the entire list and check whether that value satisfies our condition.
When we are done, the desired value will be in the `found` variable, or found will have the value `None`.

```python
found = None
for item in my_list:
    if ___:
        found = item
```

#### The Take Pattern

We have a list of items, and we want a copy of the items up until a certain point.
We again have to walk through the list, but this time we will stop taking elements
after we satisfy our condition.
Notice that the body of this loop is more complicated, using an `elif` statement
to prevent us from taking elements after we have met the condition.

```python
taking = True
new_list = []
for item in my_list:
    if ___:
        taking = False
    elif taking:
        new_list.append(item)
```

#### The Min/Max Pattern
The last pattern is used to find the highest or lowest element in a list.
This pattern is similar to the Find pattern.
However, you can see that the conditional compares each value to the accumulated value.
Using this pattern, the accumulated value (in this case a maximum) will end up as the highest value in the list.

```python
maximum = a_list[0]
for item in a_list:
    if item > maximum:
        maximum = item

print(maximum)
```

> The `a_list` variable must have a non-empty list!
