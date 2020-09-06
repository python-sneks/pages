---
waltz:
  title: Reference- Types
  resource: page
  published: true
---
Static type annotations are a powerful new Python feature that can improve
your code's readability and catch errors. By adding type information to your
code, you can give Python more information about what your code is trying to
do.

# Table of Contents

  * [Table of Contents](#table-of-contents)
  * [Basics](#basics)
  * [Types](#types)
    * [Primitive Types](#primitive-types)
    * [Container Types](#container-types)
    * [Record Types](#record-types)

# Basics

All values have a type. Variables can have values. Technically, Python
variables do not have types - you can change the value of variables to
anything you want, so you can change the type any time you want. Although we
usually say something is a "string variable" or an "integer variable", we're
really saying that we just expect that variable to have a string value or
integer value.

Static types allow us to tell Python what type of value will be in a variable.
However, Python won't do anything with that information on its own. Certain
programming environments (like BlockPy and PyCharm) know how to use that
information to give better feedback. Other environments, like Thonny, just
throw the extra information away. This is why Python calls them "type hints" -
they are not rules, but guidelines that you can break.

Although you can add type hints to variables, we will not do so. Instead, we
will use them for functions when defining the header

```python

def reverse_words(message: str, limit: int) -> str:
    pass

```

Notice the use of colons (`:`) and the arrow (`->`).

# Types

This section lists all the valid types that you can use when writing
documentation.

## Primitive Types

The following primitive types are usable as type annotations:

  * Strings: `str`
  * Integers: `int`
  * Floats: `float`
  * Booleans: `bool`
  * None: `None`
  * File: `file`
  * Any: `object`

## Container Types

Here is a list of the container types:

  * Lists: `list`
  * Dictionary: `dict`
  * Tuples: `tuple`
  * Sets: `set`
  * Callables: `callable`

These types would allow ANY type of list/set/dictionary/etc. to be used. Both
lists of integers and lists of strings would be fine. You can be more specific
by using literal syntax instead, as follows.

### List Type

To create a list annotation, wrap the type in square brackets:

  * List of integers: `[int]`
  * List of strings: `[str]`
  * List of list of strings: `[[str]]`

```python

def strs_to_ints(list_of_strings: [str]) -> [int]:
    pass

```

### Dictionary Types

To create a dictionary annotation, wrap the type in curly braces:

  * Dictionary mapping integers to strings: `{int: str}`
  * Dictionary mapping strings to integers: `{str: int}`
  * Dictionary mapping strings to lists of integers: `{str: [int]}`

```python

def names_to_ages(names: [str], ages: [int]) -> {str: int}:
    pass

```

### Tuple Types

To create a tuple annotation, wrap the type in parentheses:

  * Tuple of integer, integer, string: `(int, int, str)`
  * Tuple of string, integer: `(str, int)`
  * Tuple of list, list of strings: `(list, [str])`

```python

def get_min_max(values: [int]) -> (int, int):
    pass

```

### Set Types

To create a set annotation, wrap the types in curly braces:

  * Set of integers: `{int}`
  * Set of strings: `{str}`
  * Set of tuples of strings, integers: `{(str, int)}`

## Record Types

Records are a way to represent more complex data that has parts. They can be
used with both classes and dictionaries. They are defined with the class
syntax.

```python

class Person:
    name: str
    age: int
    is_student: bool

```

Once defined, that type can be used subsequently in the program to give type
annotations for complex dictionaries with specific keys.

```python

def make_person(n: str, a: int, i: bool) -> Person:
    return {"name": n, "age": a, "is_student": i}

def get_age(p: Person) -> int:
    return p['age']

```

# String Literal Types

Type annotations are read by the Python compiler, even if they are not used.
The annotations must be valid Python code. In several situations, this
introduces big headaches. To avoid the most common issues, we have adopted the
syntax shown above due to its simplicity. However, in some cases we cannot
reasonably avoid the complexity. For that reason, you can always write a type
explicitly as a string literal value.

```python

def reverse_words(message: 'str', limit: 'int') -> 'str':
    pass

```

## Recursive Type

When a record is recursive, it needs to use its own type in its definition.
This causes a circular dependency that Python won't know how to resolve.
Therefore, if you ever need to define a recursive type, you need to use a
string literal value.

```python

class Node:
    value: int
    next: 'Node'

```

## Conventional Typing

The built-in Python `typing` module is the most popular form of type hints.
Our alternative syntax is more convenient, but not compatible with
professional tools. We attempt to support both where possible, but we have
several extensions for pedagogical purposes.