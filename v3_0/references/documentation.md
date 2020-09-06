---
waltz:
  title: Reference- Documentation
  resource: page
  published: true
---
There are a few major ways to document functions in the Python community. We
will use the same style that Google uses, because it is popular and easy to
read.

# Table of Contents

  * [Table of Contents](#table-of-contents)
  * [Basics](#basics)
    * [Function Description](#function-description)
    * [Args](#args)
    * [Returns](#returns)
  * [Types](#types)
    * [Primitive Types](#primitive-types)
    * [Container Types](#container-types)
    * [Union Types](#union-types)
    * [Record Types](#record-types)

# Basics

All functions need to be documented. The documentation goes inside the body of
the function on the first line, indented with 4 spaces. You should use a
triple quoted string (either ''' or """), and indent the body of the string to
the same level as the body of the function.

```python

def reverse_words(message, limit):
    '''
    Consumes a `message` and produces a new string where the words have been
    reversed, up until the `limit` is reached.

    Args:
        message (str): The string of text, expected to have words separated
            by spaces (e.g., "Welcome to my lair.").
        limit (int): The maximum number of words to reverse.
    Returns:
        str: The modified version of the message.
    '''

```

There are three major sections:

  * The function description
  * The `Args:`
  * The `Returns:`

## Function Description

Often, beginners want to know how long a description they should write. If the
name of your function is really good or it is particularly obvious, it may
feel silly to have to write a long description. However, writing good
explanations of functions often pays off in the long run. Your goal is to
concisely explain the behavior while being sure to capture any surprising
behavior of your function.

## Args

Each parameter needs to be documented on its own line. The format is always
the same:

```python

name (type): description

```

  * The `name` must match the name given in the function's definition.
  * The `type` must be a valid Python type. Refer to the other sections of this document for more information on types.
  * The `description` should be a short message that accurately explains the purpose of the variable, similar to the way you create the description of the overall function.

If the function doesn't consume anything, you can skip adding the `Args:`
section.

## Returns

The last bit of your documentation is the explanation of what your function
returns:

```python

type: description

```

This is just like the Args section, but doesn't have a `name`. Hopefully that
seems reasonable, since functions don't produce variables.

If the function doesn't return anything, you can skip adding the `Returns:`
section.

# Types

This section lists all the valid types that you can use when writing
documentation.

## Primitive Types

The following are all the primitive types we recognize:

  * Strings: `str` or `string`
  * Integers: `int` or `integer`
  * Floats: `float`
  * Booleans: `bool` or `boolean`
  * None: `none`
  * File: `file`

We also support a few special built-union types:

  * Numbers: `num`, `number`, or `numeric` represents both `int` and `float`.
  * Any: `any` will match to any possible type.

## Container Types

Here is a list of the container types:

  * Lists: `list`
  * Dictionary: `dict` or `dictionary`
  * Tuples: `tuple` or `pair`
  * Callables: `callable` or `function` or `func`
  * Optionals: `optional` or `maybe`
  * Sets: `set`

All container types can optionally have a subtype using square brackets:

  * Lists: `list[int]`
  * Dictionary: `dict[str: int]`
  * Tuples: `tuple(int, str, bool)`
  * Callables: `func[(int, str) -> bool]`

You can even nest containers:

```python

list[dict[int: func[(bool, int) -> int]]]

```

## Union Types

Sometimes you need to express that a parameter or return value could be
multiple types. Although a value can only be of one specific type, the range
of values that are valid for a parameter can be more than that of a single
type. You can write `type1 or type2` to capture these kinds of relationships.

```python

def average_scores(a_list_of_scores):
    '''

    Args:
        a_list_of_scores (list[int]): The list of values to summate and then find
            the average of.
    Returns:
        int or str: If successful, returns the average. Otherwise, if the list
            was empty, returns the string value "EMPTY LIST".
    '''

```

## Record Types

Sometimes, dictionaries are used as Records, where strings are mapped to a
variety of types. If you stick to the rules above, then that dictionary's type
is simply `dict[str:Any]`, which isn't very informative.

Instead, you can use the following style to more clearly document a frequently
appearing Record type. This triple-quoted string belongs at the top of your
Python file without any indentation.

```python

'''
Records:
    Person:
        name (str): The name of the person.
        age (int): The age of the person in years.
    School:
        name (str): The name of this university.
        students (list[Person]): The people taking classes at this university.
        teachers (list[Person]): The people teaching classes at this university.
'''

```

  * You begin with a `Records:` section, and then each new Record is indented on it's own line.
  * Each new Record has its type name written out, followed by a colon.
  * Indented below that Record is each key of the dictionary, with its type in parentheses followed by a colon and a quick description.
  * Normally, dictionary keys are allowed to be any valid strings - however, this documentation style prohibits using parentheses and colons in the key.

Afterwards, you may use new type definitions elsewhere, as if that type were
declared.

```python

def create_people(names, ages):
    '''
    Create a list of people based on the given names and ages.

    Args:
        names (list[str]): The peoples' names.
        ages (list[int]): The people's ages.
    Returns:
        list[Person]: The created people.
    '''

```

Note that none of this has any impact on your actual code. Python ignores
comments and documentation, so this doesn't prevent you from building up one
of these dictionaries incorrectly. They are only used to help other
programmers understand your code.