
[Download slides](https://udel.instructure.com/files/74606266/download){: .instructure_file_link .instructure_scribd_file }


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/KziasbHkDxY?feature=oembed&amp;rel=0" 
></iframe>


#### Purpose

In some ways, computers are just large machines for doing arithematic.
Computers are very, very good at doing math.
In fact, modern computers can perform billions or even trillions of calculations per second.

> A picture of a massive super computer, with a thought bubble that reads "2+2"

#### Operators

There are six basic mathematical operators in Python that you should be familiar with:
Addition, Subtraction, Multiplication, Division, Exponentiation, and Modulo.

> A series of 6 Python math operators on the left, with arrows pointing to their names on the right.  
> `+` -> Addition  
> `-` -> Subtraction  
> `*` -> Multiplication  
> `/` -> Division  
> `**` -> Exponentiation  
> `%` -> Modulo

#### Addition and Subtraction

Addition (+) and Subtraction (-) are used for addition and subtraction.

> The subtitle "Addition (+)" followed by examples of addition and the result.
```python
> 1 + 1
```
    2
```python
> -10 + 10
```
    0
> The subtitle "Substraction (-)" followed by an example of subtraction and the result.
```python
> 5-8
```
    3

#### Multiplication and Exponentiation

One asterisk (*) is used for multiplication.
Two asterisks (**) are used for exponents (also known as powers).

> The subtitle "Multiplication (*)" followed by examples of multiplication and the result.
```python
> 4 * 2
```
    8
```python
> -5 * 5
```
    -25
> The subtitle "Exponentiation (**)" followed by an example of exponentation and the result.
```python
> 2 ** 4
```
    16

#### Division

The forward slash is used for division.
When you divide two integers, you will get a floating point number.
I'll say that again - whenever you do division, the result will always be a float!
Keep in mind, you cannot divide by 0!

> The subtitle "Division (/)" followed by examples of division and the result.
```python
> 3/12
```
    0.25
```python
> 1/1
```
    1.0
```python
> 2.5/.5
```
    5.0
    
> An annotation of the `1/1` expression points out that division always results in a float (`1.0` in this case).

#### Modulo

You have probably never heard of the Modulo operator, but it's simple: it calculates the remainder.
Modulo is sometimes called "Clock Arithmetic", because it makes it easy to figure out time.
If someone said "It is 16pm", you could do "16 modulo 12" and find out they meant "4pm".
However, modulo has many other uses, such as for figuring out if numbers are even or odd.

> The subtitle "Modulo (%)" followed by examples of modulo and the result.
```python
> 16 % 12
```
    4
```python
> 4 % 2
```
    0
```python
> 5 % 2
```
    1
    
> An annotation points out that "Modulo by 2 results in 0 or 1, indicating even or odd."

#### Using the Operators

When you run a program with operators, Python will do the math and then replace the result.
You will not be able to see the computer do the math by looking at just the code!
Notice the difference between the code on the left, and the actual actions that occur on the right.

> On the left, the subtitle "Code" is above an expression:
```python
> 2 + 3 + 4
```
> On the right, the subtitle "In the computer's head" is above the following series of simplifications: `2+3+4` becomes `5+4` becomes `9`.

#### Order of Operations
When you use operaters, there is an order of operations.

* Parentheses
* Exponent
* Multiplication, Modulo, Division
* Addition, Substraction

Whenever there's a tie, the left-most operation happens first.
Notice that you can always override any ordering by using parentheses.
You might already be familiar with this order: if not, here is a useful mnemonic:
PEMMDAS: Please Excuse My Most Dear Aunt Sally.

> The following is written out:  
> Please (Parentheses)  
> Excuse (Exponents)  
> My (Multiplication)  
> Most (Modulo)  
> Dear (Division)  
> Aunt (Addition)  
> Sally (Subtraction)
