
[Download slides](https://udel.instructure.com/files/78540252/download){: .instructure_file_link .instructure_scribd_file }


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/9CBPTykKAQE?feature=oembed&amp;rel=0" 
></iframe>




#### Documenting Code

Programmers write documentation in order to explain what a function does.
This is useful not only for sharing code with other programmers, but when we come back to code we wrote later.
To document code, you create comments that are ignored when the code is executed.
These comments are for the benefit of humans, not the computer.
Python has two ways of writing comments.

1. For sharing code
2. For re-reading old code
3. To organize our current code

#### Single-line Comment

To make a single-line comment in Python, you should use the hash symbol (also known as "pound" or "octothorpe", written as #).
Everything after the hash symbol on the same line is completely ignored by your program.

```python
# This line is ignored
a = 0 # The rest of this line is ignored
b = 0
```

> An annotation points out that following are the same: "Octothorpe", "Pound", "Hash", #

#### Multi-line Comment

To write multi-line comments in Python, you actually create a triple-quoted string. 
When Python evaluates this string, the value is unused, so it is safely ignored by the computer.
However, unlike the single-line comment, that means that the start of a multi-line comment must respect indentation rules as shown here.

> The following code is described as "Safely commented out":
```python
'''
All of this code has been commented out!
Or rather, turned into a string.
age = 0
name = "Klaus Bart"
'''
```

> The following code is described as causing an "IndentationError":
```python
def my_function(x:int, y:int)->int:
'''
The start of this string
needed to be indented!
'''
```

#### How Much to Comment?

There are many opinions on when to write comments, and no "correct answer".
Some people believe you need to document every single line.
Some people believe you should only document functions and programs as a whole.
You will need to find your own balance - for example, rather than documenting every line, you might only document lines that are particularly confusing, or document a chunk of code.

* High: Every line of code
* Medium: Some lines of code
  * Confusing lines of code
  * Large chunks of code
* Low: Only Functions

#### Documenting functions

Many people agree that, at a minimum, you should document all your functions.
Here is the convention that you will need to follow.
Use a triple-quoted string as the first line in the definition of the function.
Begin with a quick description of what the function does.
Leave a blank line, and then type "Args:".
Indent the next line, and then type the name of the first parameter followed by its type in parentheses. On the same line, write a colon and then describe the parameter. If you need to continue onto the next line, make sure it is indented past the previous line.
You should repeat this for all the parameters of your function.
Finally, write "Returns:" and then on the next line write the name of the return type, followed by a colon and a description of the returned value.

```python
def fix_capitalization(title:str)->str:
    '''
    This function capitalizes the first letter of each
    word in the title, correctly ignoring prepositions.
    
    Args:
        title (str): A book or movie title
            that we want to fix.
    Returns:
        str: The corrected title
    '''
```
