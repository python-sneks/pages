
[Download slides](https://udel.instructure.com/files/74602998/download){: .instructure_file_link .instructure_scribd_file }


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/crEA3O7qGao?feature=oembed&amp;rel=0" 
></iframe>


#### Phases of a Program

Every program has three main phases: 
The inputs are given to the program, processing occurs, and outputs are returned.
The Inputs and Outputs are how we connect programs to the real world.

> A sequence of boxes marked "Input", "Processing", and "Output"

#### Programming Is Like Baking

Think of it like baking.
The inputs are your ingredients.
Mixing and stirring are the processing.
Then the cake is your output.

> A sequence of three pictures with arrows connecting them. From left to right, there are ingredients (labeled "inputs"), a woman baking ("processing"), and a cake ("outputs").

#### Inputs

Examples of input are data typed by a keyboard, movements made by your mouse, data from the internet, and data from sensors.

> Pictures of a mouse, keyboard, and some kind of USB stick with a sensor on it.

#### Outputs

Examples of output are pixels on your screen, paper out of your printer, or the movement of a robotic arm.

> Pictures of a monitor, printer, and a robot.

#### Console

Computers take in data from users and put out results.
One of the most common ways to do this is the console.
You can think of the console as like a messenger box, for giving instructions to the computer.

> Picture of a chat window between a human and a computer. The messages read:  
> "Computer, do the thing"
> "Yes sir, I've done the thing."
> "Great work, computer"
> "Thanks, human."

#### Code

The instructions that we write are often stored in a program, so that they can be reused.
This is what "programs" or "code" really is.
Now let's learn how to write a very simple program by learning two kinds of commands: "Print" and "Input".
We will see these two commands as regular Python text, but also as BlockPy blocks.

> A picture of a piece of paper with lines coming out annotating it with the words "print" and "input", representing how instructions are stored as text in a program.

#### Print

The "print" function lets you write information to users.
Printing is necessary because we cannot see "inside" the mind of the computer, except what it writes on the console.
Notice that there is some text between the parentheses: this is the text that is output to the user.

> Some code is shown on the screen in both block and text form.  

```python
print("This will be shown to the user")
```

> An annotation notes that "Only the text INSIDE the quotation marks will be printed!"

#### Input

The "input" function lets you get information from users.
Notice that there is some text between the parentheses: this is the text that is shown as a prompt to the user.
Once the prompt is shown, the user can type their answer and press enter.

> Some code is shown on the screen in both block and text form.  

```python
input("This will be shown to the user")
```

#### A Simple Program

Notice how we can combine these two commands by snapping them together.
This simple program will take some text from the user and then print it out.
While not a very exciting program, it is a great example of the input/output mechanism of programs.

> Some code is shown in both block and text form:

```python
print(input("This will be shown to the user"))
```

> Then, an arrow (annotated with the Run button) shows how the result will be printed on the Console in BlockPy, if the user enters `I typed some text!`

    This will be shown to the user
    I typed some text!

#### But Why?

The goal of any program is to transform the inputted data into the desired outputs.
For now, our programs will have simple inputs and simple outputs.
But eventually, we will create complex code that can achieve great things.

> On the left, a circle is labeled "Types of Data", with smaller circles sticking out - these smaller circles are labeled nouns like "geographical", "financial", "scientific", "statistical", and "cultural".  
> On the right, an arrow labeled "Python" points to a person thinking.
