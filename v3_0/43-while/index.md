# While Loops

[Download slides](While%20Loops.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/YEJr-vIpLP4?feature=oembed&amp;rel=0" ></iframe>


#### Another Kind of Iteration

FOR loops allow us to iterate through each element of a list.
They are the most common form of iteration in Python.
However, there is another kind of iteration that is useful, called While loops.

```python
while condition:
    pass
```

#### Syntax
Notice how the syntax for a WHILE loop is similar to that of an IF statement.
We have the word WHILE, followed by a condition, ending with a colon.
Then we can have any number of statements inside the body.
Remember that this body, like a FOR loop or an IF statement, is indented with 4 spaces.

> The following code is annotated with the terms "While keyword", "Conditional", "Colon", and "Body":

```python
while condition:
    pass
```

#### Like IF Statements

`while` loops are actually very similar to `if` statements.
However, instead of executing once or none, they will execute repeatedly until the condition is false.
Note that a loop won't end until the condition evaluates to false - even if the condition would be false during the loop body, the loop can't end until the end of the body.


> An arrow traces the flow in the code below, with a branch at the end of the loop's body: one branch moves back up to the start of the loop, and the other moves further downward.

```python
count_down = 4

while count_down > 0:
    count_down -= 1
    print(count_down)
    
print("Reached the end")
```

#### Tracing the Flow

When a While loop is executed, the program follows a similar looping behavior as a FOR loop.
Here we can see that behavior in a WHILE loop to count down from 10.
The program tests the condition, and if it is true, then it moves through each statement in the body.
Then, it returns to the top and tests the condition again.
If it is still, true, it repeats the previous loop. Otherwise, it skips to the end of the WHILE body.

> The cdoe from before is shown in an [interactive PythonTutor session](http://www.pythontutor.com/visualize.html#code=count_down%20%3D%204%0A%0Awhile%20count_down%20%3E%200%3A%0A%20%20%20%20count_down%20-%3D%201%0A%20%20%20%20print%28count_down%29%0A%20%20%20%20%0Aprint%28%22Reached%20the%20end%22%29&cumulative=false&curInstr=15&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).

#### Looping Forever

A tricky thing about WHILE loops is that it is easy to loop forever by accident.
Consider the code below.
Because the variable `count_down` is only ever increasing, it will never reach zero and the loop never ends.

> An annotation points out that the first line of the loop only increases the variable, so it never reaches 0.

```python
count_down = 4

while count_down > 0:
    count_down += 1
    print(count_down)
    
print("Reached the end")
```

#### Unnecessary While Loops

A major advantage of For Loops instead of While Loops is that they terminate based on a list, so they are very unlikely to loop forever.
When possible, you should probably use a FOR loop instead of a WHILE loop.
As an example, consider the counting code shown before.
Instead, that can be efficiently replaced with a FOR loop that calls the "range" function, which consumes a integers and produces a list of integers counting up to that number.

> `while` Loop version:

```python
index = 0
while index < 10:
    index += 1
    print(index)
```

> `for` Loop version:

```python
for index in range(10):
    print(index)
```

#### User Input Loop

One of the very few cases where a `while` loop is more useful than a `for` loop is dealing with repeated user input.
For instance, the Read-Evaluate-Print-Loop that powers a command line uses a `while` loop.
The pattern shown here is one way to handle repeated user input.
This repeatedly asks for words until the string `"EXIT"` is given, at which point it will exit the loop.


```python
command = ""
while command != "EXIT":
    command = input("Input a word, or write EXIT:")
    print("You wrote", command)

print("No more words!")
```

