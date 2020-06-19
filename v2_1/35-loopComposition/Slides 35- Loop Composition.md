# &icon-ms-ppt; Slides

[Download slides](https://udel.instructure.com/files/78929708/download){: .instructure_file_link .instructure_scribd_file }

# &icon-video; Video

<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/iWMunO9dNp0?feature=oembed&amp;rel=0" 
></iframe>

# &icon-document; Transcript


#### Indirectly Looping in Functions

You can calculate the mean, or average, of a list by adding together the elements and dividing by the number of elements.
Finding the average is a common operation for a list.
You could write this function by creating a loop that combines the Sum and Count patterns.
Alternatively, you could define functions to sum and count, and then use those functions in your Average function.
This version does not require a loop directly in the Average function, because the loop happens indirectly in a helper function.

> Looping version

```python
def average(nums: [int]) -> float:
    sum = 0
    count = 0
    for num in nums:
        sum = sum + num
        count = count + 1
    return sum / count
```

> Indirectly looping version

```python
def sum(nums: [int]) -> int:
    sum = 0
    for num in nums:
        sum = sum + num
    return sum

def count(nums: [int]) -> int:
    count = 0
    for num in nums:
        count = count + 1
    return count

def average(nums: [int]) -> float:
    return sum(nums) / count(nums)
```

#### Functional Decomposition

Earlier, we learned to break up complex functions into multiple parts using functional decomposition.
With loops, we finally see why that becomes necessary.
The control flow for a function with a loop is complicated.
When you start nesting loops and if statements inside of functions, mistakes are likely.
Functional decomposition allows us to tame that complexity by focusing on one conceptual step at a time.

> A diagram showing how a main function is decomposed into calls to several helper functions.

#### Complex Combinations

Let's say that we wanted to add up all the negative numbers in a list.
You could write a for loop that combines the Filter pattern and the Count pattern.
You might even succeed.
But what if you also needed to convert all the elements from strings to integers first?
What if you needed to also find the average?
Suddenly, combining all these patterns becomes difficult.

> A person is shown thinking about the many different actions they must take.

#### Composing Loop Patterns

Instead, let's focus on defining functions to solve each part of the puzzle in turn.
We define a `map_strs_to_ints` function that maps string conversion over a list of strings.
We define a `remove_negatives` function that filters out negative integers.
We define a `count` and `sum` function that consume lists of integers to accumulate.
Then, we can compose those functions as needed into an `average_positives` function.
This may seem like a lot more work - suddenly we have to define and test 5 functions instead of 1.
But the advantage is that each function is relatively easy to define and test.
If you make a mistake, you will be able to track it down very quickly.


```python

def map_strs_to_ints(numbers: [str]) -> [int]:
    ...

def remove_negatives(numbers: [int]) -> [int]:
    ...

def count(numbers: [int]) -> int:
    ...

def sum(numbers: [int]) -> int:
    ...
    
def average_positives(numbers: [str]) -> float:
    numbers = remove_negatives(map_strs_to_ints(numbers))
    average = sum(numbers) / count(numbers)
    return average
```