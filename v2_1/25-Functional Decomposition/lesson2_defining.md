# Example Function Definition

## Example
The code below converts a temperature from Fahrenheight to Celsius.
This code has some issues, however.
First, the calculation is called multiple times in the code, which makes it much more likely for a mistake to occur when typing it.
Second, if a mistake does occur, it will be harder to track down in the offending lines.
Third, anyone not familiar with the formula might wonder what this code is doing.
A function will help us with all of these problems.

## 1) Start the Definition
We begin with the skeleton of a function. 
In BlockPy, the Function block generates this function, ready for editing.

## 2) Name the function
If you cannot name a function, then you probably don't know what it should do.
We know that this function will convert a temperature, so let's call it convert_temperature.
This name is short and has a verb.
Notice how I used underscores to represent spaces, because function names follow the same rule that variables do.

## 3) Find Commonalities
You need to identify what is the same and what is different about each call.
Extract out the code that is the same.
Here, we've extracted out the calculation.

## 4) Parameterize
Notice the blank in the code we extracted.
Since this was different each time, we need to parameterize it by giving those concrete values a more general name.
In this case, each time it was a temperature in fahrenheight, so we'll call this "fahrenheight_temperature".
We put this new parameter in the function's header and then use it in the body.

## 5) Return
The code we've created is meant to go inside the body of the function, but we have nothing to connect it to yet.
Recall that this function should return the temperature in celsius.
Therefore, we need a return block.
This gives us an open connection.

## 6) Call
Finally, we can now call our function in the code.
Notice how we connect the original values as arguments for our function call.

## Other Approach
Here, we turned existing code into a function definition and then called the function.
Another common approach is to do the opposite: write the function call, and then use that to write the function definition.
Use whichever order is more comfortable for you when solving each problem.

## Watch the Execution
So what actually happens when you call a function?
Let's see it in action.

## Keywords
We have now learned a few keywords: def, return, and pass.
In previous lessons, we learned a few other keywords: and, or, not, and in.
Python has a small set of keywords, and you will eventually learn most of them.
An important detail to remember is that we cannot name variables or functions using keywords, because Python will get confused by what we are trying to say.

## Functional Decomposition
When writing out a solution, you can use a powerful tool called Functional Decomposition.
The idea is to break a complex problem into easier parts.
Consider the task of going to the store.
You could break this long algorithm into three shorter subtasks, and focus on solving each in turn.
{ "Going to Store" -> "Get to Car", "Drive Car to Store", "Exit Car into Store"}

## Questions
- You have been tasked with creating a function that opens a garage door. Which of the following a good, valid name?
    - ogd, a short abbreviation that saves many letters when typing.
    - open_garage_door, a concise name that captures the idea
    - open garage door, a concise name that captures the idea
    - door, a short name that captures the idea
    - openThePodBayDoorsHal, a fun reference to a classic sci-fi movie

## Problems
- The code below has a problem with the function call. Try running the code, and observe the output. Then, fix the function call. (bad parentheses)
- The expression below calculates the volume of a cylinder. Extract the expression into a function named <code>calculate_volume</code>.
- The expression below extracts the first half of a string by using the <code>len</code> built-in function. Extract the expression into a function.
- Write a function <code>to_pig_latin</code> that converts a string into pig latin, by putting the first character at the end of the string and adding "ay" to the end. Call the function twice to demonstrate the behavior.
- <p>The formula below calculates the distance between two points in an XY plane.</p>
<pre>distance = ((y2-y1)<sup>2</sup> + (x2-x1)<sup>2</sup>)<sup>.5</sup></pre>
<p>Rewrite the formula as a function <code>calculate_distance</code> with the parameters <code>x1</code>, <code>y1</code>, <code>x2</code>, <code>y2</code>.</p>
- <p>In the real world, it is easy to be fooled by the description of a problem into thinking that you must use a certain function or method, just because you see a certain word. Keep that in mind for this problem</p>
<p>Write a function <code>hide_letter</code> that replaces the first character of a string with the symbol <code>"?"</code>. So <code>"Apple"</code> will become <code>"?pple"</code> and <code>"1234"</code> will become <code>"?234"</code>. Call this function twice.</p>