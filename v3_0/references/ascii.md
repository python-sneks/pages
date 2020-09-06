---
waltz:
  title: Reference- ASCII Table
  resource: page
  published: true
---
The American Standard Code for Information Interchange (ASCII) is a way of
representing text via numbers. Every single character is represented via a
different number. Although modern systems require a larger set, the basic
ASCII table has remained relatively unchanged since it was created in the
1960s. The system is critical to sending storing and transmitting textual
data. You can read more about the history of [ASCII
here](https://en.wikipedia.org/wiki/ASCII).

# The Ord Function

To convert a single character (string) to an integer, use the built-in `ord`
function. This function consumes a string and produces an integer. The string
must be exactly one character long, or you will get a TypeError.

```python

ord("A")
# 65

ord("a")
# 97

ord("FF")
# TypeError!

ord("6")
# 54

ord("!")
# 33

```

# The Chr Function

To convert an integer back to a character (string), use the built-in `chr`
function. This function consumes an integerand produces a string. The integer
must be a positive number, or you will get a `ValueError`. Values outside of
the range 32-126 are not printable, and may look weird when you try to convert
them.

```python

chr(65)
# "A"

chr(97)
# "a"

chr(-1)
# ValueError!

chr(54)
# "6"

chr(33)
# "!"

```

# The ASCII Printable Characters

Codes 32-126 are common for all the different variations of the ASCII table.
They are called printable characters, representing letters, digits,
punctuation marks, and a few miscellaneous symbols. You will find almost every
character on your keyboard.

Below, you can see all of the printable ASCII characters and their decimal
representations.

Character | Decimal  
---|---  
| 32  
! | 33  
" | 34  
# | 35  
$ | 36  
% | 37  
& | 38  
' | 39  
( | 40  
) | 41  
* | 42  
+ | 43  
, | 44  
- | 45  
. | 46  
/ | 47  
0 | 48  
1 | 49  
2 | 50  
3 | 51  
4 | 52  
5 | 53  
6 | 54  
7 | 55  
8 | 56  
9 | 57  
: | 58  
; | 59  
< | 60  
= | 61  
> | 62  
? | 63  
@ | 64  
A | 65  
B | 66  
C | 67  
D | 68  
E | 69  
F | 70  
G | 71  
H | 72  
I | 73  
J | 74  
K | 75  
L | 76  
M | 77  
N | 78  
O | 79  
P | 80  
Q | 81  
R | 82  
S | 83  
T | 84  
U | 85  
V | 86  
W | 87  
X | 88  
Y | 89  
Z | 90  
[ | 91  
\ | 92  
] | 93  
^ | 94  
_ | 95  
` | 96  
a | 97  
b | 98  
c | 99  
d | 100  
e | 101  
f | 102  
g | 103  
h | 104  
i | 105  
j | 106  
k | 107  
l | 108  
m | 109  
n | 110  
o | 111  
p | 112  
q | 113  
r | 114  
s | 115  
t | 116  
u | 117  
v | 118  
w | 119  
x | 120  
y | 121  
z | 122  
{ | 123  
| | 124  
} | 125  
~ | 126