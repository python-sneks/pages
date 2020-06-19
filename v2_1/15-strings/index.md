
[Download slides](Strings.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/daoY8lLoSAk?feature=oembed&amp;rel=0" 
></iframe>


#### Purpose

Strings are how we put text data into a computer.
Any text data can be a string: names, words, books, web sites.

> Example name, Example words, example book }

#### Characters

Strings are made up of letters, numbers, and symbols.
We call these things "characters".

> Letters, Numbers, and symbols

#### The name "String"

Think of a String like a necklace, where each bead has a character on it.
We "string together" letters.
The single or double quotes are knots at the end that tie the letters off.

> String as a string of beads

#### Notation

Strings are represented with quotes.
You can use either double quotation marks or single quotation marks.
However, if you start a String with double, you must end with double.
If you start with single, you must end with single.
The reason there are two kinds is to make it easier to create strings like the below

> Left: `"What's wrong with me?"`, with a mark on the `'`  
> Right: `'He said, "What did you do?"'`, with a mark on the `"`

#### Escape Characters

So how do you have a string with both single and double quotes in it?
You can use escape characters.
By putting a back-slash "\" before a character, you create a special character.
Check out the example below:

    `"He said, \"What's wrong with me?\" to the girl."`

There are actually many kinds of escape characters:

* `'\n'` is a new line (like pressing enter)
* `'\t'` is a "tab" character, or multiple spaces (like indenting a paragraph)

> `"This will be\ntwo lines of text."`  
> `"This will have\tsome blank space."`

#### Numbers and Strings

It's a little confusing, but you can put a number in quotes.
However, this means that you have a string and not an integer.
The difference becomes very obvious when you try to add things together.
`"1" + "2"` is `"12"`, instead of `3`.
Python is very strict about the differences between Numbers and Strings.

> These are strings, not integers!  
> `"1" + "2"` is `"12"`

#### Variables and Strings

Some people confuse Variables and Strings, but they are very different.

> A string value (right) being assigned to a variable (left).

```python
my_string_variable = "A string value"
```

#### Triple Quoted Strings

Rarely, you have to put a huge amount of text into your program. The best way
to do so is to use "triple quoted strings". The syntax is simple: you start and
end the chunk of text with three quote marks. It doesn't matter if they are
single or double quotes, as long as it starts and ends the same.

```python
my_variable = """This is a long multi-line 
text block. Notice how it can spill onto 
multiple lines. It has been assigned to a new 
variable called my_variable."""
```
