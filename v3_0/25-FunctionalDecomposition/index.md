
[Download slides](Functional%20Decomposition.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/Ta9Zdy50IP8?feature=oembed&amp;rel=0" 
></iframe>




#### Functional Decomposition

When writing out a solution, you can use a powerful tool called Functional Decomposition.
The idea is to break a complex problem into easier parts.
Consider the task of going to the store.
You could break this long algorithm into three shorter subtasks, and focus on solving each in turn.

> On top, a box is labelled "Going to the Store".  
> On the bottom, this box is subdivided into three more boxes:  
> Get to the car, drive car to store, exit car into store.

#### Split Up Complex Functions!

Let's take a concrete example.
On the left, we see some code that needs to do a series of tasks.
On the right, we have split that one function into three separate pieces, each of which could be tested independently.
Then, we rewrite the original function to use our new functions.

```python
def is_user_freezing(text:str)->bool:
    celsius = int(text[-2:])
    fahrenheit = (celsius*9/5) + 32
    return fahrenheit < 32
```

> Becomes

```python
def capture_temperature(text:str)->int:
	return int(text[-2:])

def to_fahrenheit(celsius:int)->float:
	return (celsius*8/5) + 32

def is_freezing(temperature:float)->bool:
	return temperature < 32

def is_user_freezing(text:str)->bool:
    celsius = capture_temperature(text)
    fahrenheit = to_fahrenheit(celsius)
    return is_freezing(fahrenheit)
```

#### Functional Decomposition is Powerful!

It may seem like Functional Decomposition is just giving yourself more work. 
Now you have to unit test and document extra functions?
Why not just do all the work in a single function?
The answer is that decomposition makes it easier to debug functions.
As our programs get more complex, you are more likely to make mistakes.
Breaking your functions into manageable parts is scientifically shown to increase your likelihood of success.


```python
from cisc108 import assert_equal

def to_fahrenheit(celsius:int)->float:
	return (celsius*8/5) + 32

assert_equal(to_fahrenheit(40), 104.0)
```

> An annotation points out that the unit test fails with this error:

    FAILURE, predicted answer was 104, computed answer was 96.

> A thought bubble reads, "Ah, so this part of the function is the problem!"

#### Keywords

We have now learned a few keywords: def, return, and pass.
In previous lessons, we learned a few other keywords: and, or, not, and in.
Python has a small set of keywords, and you will eventually learn most of them.
An important detail to remember is that we cannot name variables or functions using keywords, because Python will get confused by what we are trying to say.

* def
* return
* pass
* and
* or
* not
* in
