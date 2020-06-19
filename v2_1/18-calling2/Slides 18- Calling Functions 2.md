# &icon-ms-ppt; Slides

[Download slides](https://udel.instructure.com/files/74875417/download){: .instructure_file_link .instructure_scribd_file }

# &icon-video; Video

<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/vWJCOoQxUAc?feature=oembed&amp;rel=0" 
></iframe>

# &icon-document; Transcript

#### The Many Functions
Python has many, many built-in functions.
You could never learn them all in this course.
You will learn a few, but it's far more important that you learn how to learn more about functions.

> A list of dozens of built-in Python functions are shown, including: `abs`, `bool`, `zip`, and `sorted` among many others.

#### Learning about a Function
Good programmers create documentation for their functions.
Documentation is extra information about a function that makes it clear how it works.
There are many ways to write documentation, but they usually have a few things in common.

    Name: len
    Description: The function "len" returns the number of characters in a string (its length).
    Syntax:
    	len(a_string)
    Parameters:
    	a_string (String): The string to calculate the length of
    Returns: Integer
    Example:
        len("Hello World")


#### Function Documentation
You should look for six major parts.
The function's name, its parameters, its return value, its description, and examples how to use the function.

> The same text from the previous slide with the following words circled: Name, Parameters, Return value, Description, Examples.

#### Parameters and Arguments
The Arguments that are passed into a function are also known as Parameters.
Parameters are the formal names that allow us to refer to a the function.
In the example below, the arguments are 3, 10, and "Hello".
The documentation tells us that the corresponding parameters are X, Y, and Z.

> A function call is shown:

```python
calculate_area(3, 10)
```

> With the following documentation below it:

    Name: calculate_area
    Syntax:
        calculate_area(length, width)
    Parameters:
        length (Integer): The length of the rectangle
        width (integer): The width of the rectangle
        
> Annotations indicate that the `3` and `10` are arguments, while `length` and `width` are parameters.

#### Nesting Function Calls

A common task is to nest function calls inside of other function calls.

```python
print(len("Hello World"))
```

> Arrows point from the value `"Hello World"` to the function name `len`, and then arrows point from `len` to the function name `print`.

#### Chaining Methods
When you need to call methods on the same string variable or value, it's a little different.
As shown below, you will repeat the period, name, and parenthese each time.
By placing them side-by-side, you will keep using the same variable, modifying it in turn from left to right.

```python
"hello world".title().count('o')
```

> Arrows point from the value "hello world" to the method name `title`, and then arrows point from `title` to the method name `count`.

#### Functions, Methods, and Operators

Since calls are just another expression, you can freely combine them with each other.
Observe the code show, where we combine string addition, a string method call, and a function.
Notice the order of execution, this can be tricky to follow!

```python
string_length = len("hello " + " world ".strip())
```

> The `string_length =` is labelled as an assignment statement  
> The `len(` part is labelled as a function call.  
> The `+` part is labelled as a string addition.  
> The `.strip()` is labelled as a method call.

#### Input/Output

You already know two functions:
Print is a function that takes in arguments and writes to the console.
Input is a function reads from the console and returns it as a string value.

These two functions are strange, because they have side effects.
The Input function puts a textbox on the console, and the print function writes text to the console.

> On the left, the code `print()`
> On the right, the code `input()`
