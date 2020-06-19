# &icon-ms-ppt; Slides

[Download slides](https://udel.instructure.com/files/74607812/download){: .instructure_file_link .instructure_scribd_file }

# &icon-video; Video

<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/fZ1NKT40HXE?feature=oembed&amp;rel=0" 
></iframe>

# &icon-document; Transcript

#### Purpose

When something goes wrong with your program, Python will give you an error message.
These messages are meant to help you find where your error is and what kind of error it is.

> A picture of a computer with the word "ERROR!" displayed on its monitor.

#### Types of Error Messages

Python has many, many error messages.
It can take a long time to learn them all.
When you encounter an error message you are unfamiliar with, you should first read and think about the message.
If you are not sure what it means, you should look up the error's meaning in the documentation.
Then, you can debug your program.

> A large list of the common Python errors, including `NameError`, `ImportError`, `ValueError`, `TypeError`, and `UnboundLocalError`.

#### Terminology

Just a minor point of terminology.
Errors are sometimes referred to as "Exceptions".
They're not quite identical, but for our purposes they might as well be.

> The words "Errors" and "Exceptions" are written out.

#### Identify the error type

Let's imagine that we ran some code, and encountered an error message.
In the bottom left of the error message, you can see the type of error.
In the example here, you can see that we have a "TypeError".
After the error type, there is usually some further description of the error.

> Above, we can see an error message from Thonny, with the word "TypeError" circled.  
> Below, we can see an error message in BlockPy, with the word "TypeError" circled again.

#### Find the Line

It can be tricky to read, but the error message should also identify WHERE the error occured.
Of course, sometimes the error is actually caused by code on a previous line.
You will have to think very critically about whether the error message is correct.

> The same error messages are shown from the previous slide, but this time the line number is circled instead.

#### Common Errors: NameError

Let's look at a few common errors.
First, here is a NameError.
A NameError comes up when you try to reference a variable that does not exist yet.
Sometimes, you mispelled the name of the variable.
Sometimes, you have not initialized the variable.
Sometimes, you initialized the variable, but you did so AFTER its first usage.
In this case, there is a typo in the name "student grade".

> The following code is shown:
```python
student_grade = 10
print(studetn_grade)
```
> An annotation points out that the second line has a typo (`studetn_grade`) which will cause a NameError.

#### Common Errors: TypeError

Another common error is the TypeError, which occurs when you use an operator incorrectly.
For example, adding together a string and a number is not allowed.
When you read the error message that is produced, it will describe what went wrong.
Here, it says that we attempted to concatenate (which means combine) a string and an integer.

> The following code is shown:
```python
print("7"+3)
```
> An annotation points out that the following error message will be shown: "TypeError: cannot concatenate 'str' and 'int' objects on line 1".

#### Common Errors: SyntaxError

A syntax error means that you broke Python's rules of spelling, grammar, and punctuation.
There are many ways to break a programs' syntax.
Usually, Python is very good at suggesting where the error is.
Still, sometimes it can be very tricky to track down a SyntaxError.

> The following code is shown:
```python
name = "Klaus von Wagglyschwantz"
age = 17
is_good_dog = True
print("Klaus is a good dog?)
print(is_good_dog)
```
> An annotation points out that hte following error message will be shown: "SyntaxError: bad token on line 4
Missing quotation mark".

#### Debugging Errors

We'll learn some more techniques to help you fix your broken problems in the coming weeks.
For now, think critically about the errors you receive.
When you see one you don't understand, you should ask "What does this error message mean?" instead of "What is wrong with my program?"

> A silhouette of a detective (Sherlock Holmes) looking at the computer displaying "ERROR!" on its monitor.
