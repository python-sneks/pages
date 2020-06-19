# &icon-ms-ppt; Slides

[Download slides](https://udel.instructure.com/files/76109864/download){: .instructure_file_link .instructure_scribd_file }

# &icon-video; Video

<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/WBRRQtyg1VM?feature=oembed&amp;rel=0" 
></iframe>

# &icon-document; Transcript

#### Modules

Whenever you create a new Python program, you are actually creating a Module.
In other words, a module is just a Python program.
A module is useful, however, because it can be imported into another module.
Any functions, variables, and other definitions created in the module will then be available in the other module.

> Modules are Python Programs

#### Terminology

Modules are sometimes also known as packages or libraries.
Typically, a package is a collection of one or more modules.
However, the words are all more-or-less interchangeable.

* Module
* Library
* Package

#### Import

To import data from another module, you use the Import statement.
There are three different ways to import a module.
The simplest is shown here, where we write the keyword import and the name of the module.
Once a module is imported, you can reference its definitions using the name of the module, a period (`.`), and then the name of the function, variable, or other definition you want to use.

```python
import math
```

> Annotations on the code above point out the `import` keyword and the module's name on the first line.  
> After this code is run, you can use the built-in `math` module with the module's name and a period:

```python
# Built-in square root function
math.sqrt(100)

# Built-in PI constant
math.pi
```

#### Specific Import

It can be bothersome to repeat the module name each time you want to use a function.
Therefore, Python has a convenient syntax for importing the functions directly.
This version uses the "from" keyword, followed by the module name, the "import" keyword, and then the name of the function or other definition you want to use.
Afterwards, you can use the definition as if it were defined in that file.

```python
from math import sqrt

sqrt(100)
```

> Annotations point out that the code above uses the `from` and `import` keywords, in addition to the module's name.  
> Note that we no longer need to use the module's name later in the code with the period.

#### Longer Imports

Complex packages are often divided into multiple folders containing the modules.
When importing specific parts of these packages, you will need to use periods to indicate folder names.
The result of this import is then aliased (or renamed) using the "as" keyword.
Usually, the documentation will tell you exactly what to import; otherwise it can be difficult to infer the path.
For example, many tutorials for the MatPlotLib library (which we will learn later) suggest you import the PyPlot module as shown here.
After this import, the "plt" module is now available.

```python
import matplotlib.pyplot as plt
```

> Annotations point out the `import` keyword and `as` keywords, along with the use of a package and module name, to import the module with a shortened name (`plt` in this case).

#### Standard Library

Python has a number of useful built-in modules called the Standard Library.
Further, Python programmers have created many other "third party libraries" that are easy to install.
Many of these modules come prepackaged in distributions like Anaconda.
We will not cover all these modules in this course, but you will often come across them when solving real-world problems.

> A very long list of module names, including: `random`, `statistics`, `datetime`, and many more.

## Installing New Libraries

Although you may not have to do it very often, it is very easy to install new modules from a command line.
You can use the `pip` command to install a module.
You will need to know the exact module name.
Make sure that you have the right module name; when you install a new module, you are trusting the developer to not install anything malicious!
Most modern editors, including Thonny, also include a package manager that let's you install packages without writing code.

```
> pip install pygame
> pip install requests
> pip install matplotlib
```
