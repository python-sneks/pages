This tutorial will show you how to create a Text Adventure Game using our engine. We will end up developing a game called The Spooky House which has many basic features for a Text Adventure Game. As you will see, this program is much bigger than any that we have made so far.

The tutorial is broken up into multiple parts. You should probably be modifying your own version of the project as you go, but you may find it helpful to skim through the entire thing first.

# Reviewing Big Ideas

Developing a large program is hard. You need to bring together and nest many types of data and control structures. Once your program is hundreds of lines long, it is impossible to keep everything in your head at once. We must learn to manage the complexity of our code.

Many of the skills we have learned so far are in service of building large programs.

* **Functions** allow us to reuse bits of code and chunk up related lines.
* **Functional** decomposition helps keep functions short and clear.
* **Scope** rules keep us from leaking data in one part of a program into another.
* **Immutability** prevents us from messing up data from another part of a program.
* **Unit Tests** help us confirm that a function is correct so we can determine where an error is.
* **Documentation** helps us understand what older functions do.

Sometimes, these rules are bothersome. But Computer Scientists keep using them because they are effective. As you write larger programs, keep these rules in mind.

If you don't remember what any of these terms mean, now would be a good time to review them. You might also find it helpful to review them after you read this tutorial.

# Overview of the Template

Start by looking at the `adventure_template.py` file. The file is over 150 lines long, so it is divided into 6 sections:

* Section 0 is the header, where basic instructions are given.
* Section 1 is author info, where you identify yourself and your game.
* Section 2 is for your Record definitions, to help explain the model of your game.
* Section 3 is your core game functions, which will be the actual code of your game.
* Section 4 has the win/lose paths for your game, which help the autograder play your game.
* Section 5 is the unit tests, where you will write code to confirm that your game works as intended.
* Section 6 is the main game engine, which you will not need to modify.

Next up: [The Main Game Engine](LINK)

# The Main Game Engine

Section 6 has the main game engine, which has already been written. On the plus side, you will not need to modify this engine - you only need to define the functions it uses. However, this means you may not adjust the engine if you want to change it, and you are forced to build your game in a certain way.

A dangerous mistake is to ignore the engine while developing your game. Failure to follow the requirements of the engine will result in a rejected game worth zero points. It is absolutely critical that you follow the engine's rules. When your game is completed, if you followed the engine's rules, it will be possible for us to host it online. This will let you play and share your game with anyone, even if they do not have Python. You can see some [existing games here](https://choose-your-python-adventure.herokuapp.com).

The engine itself is not very long, but it has a lot going on:

```python
def main():
    ''' ... '''
    print(render_introduction())
    world = create_world()
    while world['status'] == 'playing':
        print(render(world))
        options = get_options(world)
        command = choose(options)
        print(update(world, command))
    print(render_ending(world))

main()
```

When the `main` function is executed, the game begins:

1. An introduction is printed.
2. The initial world is created and stored in the `world` variable.
3. A `while` loop is started that will check that the world's status is `"playing"`.
4. The world is rendered (as text) and then printed to the user.
5. The current world state is used to determine the available commands, which are stored in `options`.
6. The `choose` function is used to get input from the user and choose one of the commands.
7. The `world` is updated based on the `command` chosen, and a message can be printed describing what happened.
8. Since the body is done, the condition of the `while` loop is re-evaluated; we either return to step 4 or continue onto step 9.
9. The ending is printed based on the final state of the world.

Because the main game engine is using `print`, you will never need to. Do not call `print` inside any of your game functions (unless it is for testing purposes). This is important if you want your game to eventually be playable in the browser. You also must never use the `input` function anywhere in your code, or the autograder will reject your submission.

The `choose` function is an exception to the "no printing" rule: it both prints and takes user input. Fortunately, you have already written `choose` as part of the programming problems. Use your implementation from there. All of the logic for interacting with the user is isolated to the `choose` function.

Next up: [Rendering an Introduction](LINK)

# Rendering an Introduction

The first function you can write is `render_introduction`, which consumes nothing and produces a string.
This function creates the introduction of your game; much like writing an essay, you might want to leave this until the end. This will help you create a more consistent story. However, you may also find it helpful to write up a draft version to guide your development. It is important to recognize that your game's concept will change over time. Game designers never end up using their first draft, in practice.

However, we already know what the script for the Spooky House will be, so we'll write it here. Note the use of new line characters (`'\n'`) in our string literals - otherwise the final printed result will be on one line, and we want to keep the width of each line within 80 characters. Although there are many ways to write long text blocks (e.g., multi-line strings, joining a list of string literals), we use string addition (which requires parentheses if we have multiple lines of Python code).

```python
def render_introduction():
    ''' ... '''
    return ("== The Spooky House ==\n"+
            " = By Dr. Cory Bart =\n"+
            "\n"+
            "After getting lost in the woods near your house,\n"+
            "you see a yard in the distance.")
```

## Testing

Once the function has been written, we should unit test it to make sure it works as expected. All your unit tests will go in Section 5. You might be tempted to call the function and confirm the output is as you expected.

```python

assert_equal(render_introduction(), """== The Spooky House ==
 = By Dr. Cory Bart =

After getting lost in the woods near your house,
you see a yard in the distance.""")
```

However, if you test all the text in your game this way, you will do a lot of tedious copying and pasting. Instead, you might consider testing your code with more strategic assertions:

```python
# Confirm that we printed the name of the game
assert_equal("The Spooky House" in render_introduction(), True)
# We should have 5 lines of text
assert_equal(render_introduction().count("\n"), 4)
# Make sure it explicitly mentions "your house" to set up the punchline,
#   that you've been in your own house the entire game.
assert_equal("your house" in render_introduction().lower(), True)
```

Next up: [Modeling the World](LINK)

# Modeling the World

In a [previous assignment](LINK), you were instructed to create World Definitions. Right now, review the [World Definitions for the Spooky House and Finding Adventure](LINK2). These will end up going in Section 2 as a triple-quoted string literal (the template has them already). You will use them to build your Record dictionaries. Let's look at what these definitions mean.

## World

The `World` is the most important definition, and acts as a container for all other things. It is a snapshot of the world, frozen in time. At the minimum, everyone will have three keys in this dictionary: `status`, `map`, and `player`.

The `status` field is just a string, and will only ever be one of four possible values: `"playing"`, `"won"`, `"lost"`, or `"quit"`. The game is initially in the Playing status, and then at some point will switch to one of the other statuses when the game is meant to end.

## Locations

The `map` key is associated with a dictionary that maps strings to `Location`s. The keys will be the names of locations, and the values are the data about that location.

The `player` field is associated with a single `Player` record dictionary, which helps separate information about the player from the world at large. The `location` field is connected to the keys of the `World`'s `map` field: when you want to move the player to a new location, you just update their `location` field with one of the keys from your `map`.

A location has at least three fields: `about`, `neighbors`, and `stuff`. The `about` is a simple text description that can be used to quickly describe what this location looks like. The `neighbors` are a list of strings representing locations that the player can move to from here.

## Inventory and Stuff

The `Player` has a field named `inventory` which is similar to the `Location` field named `stuff`. Both fields are a list of strings representing generic things in the world. Often, values will be moved between location's stuff and the player's inventory, as you collect and use items. Note that the inventory can be used to represent more than just items: people, skills, knowledge, and many more things can be captured in this model.

Next up: [Creating the World](LINK)

# Creating the World

The Record definitions guide the development of the next game function `create_world`, which consumes nothing and produces a dictionary. This dictionary will be an instance of the `World` we defined before. Now, however, we need to focus on what values everything should have. The `status` field is quite simple (initially `"playing"`), but the `map` and `player` field will be very complex. We're going to use Functional Decomposition to guide our development: we'll create additional functions ("helper functions") to break up the work being done.

```python
def create_world():
    return {
        'map': create_map(),
        'player': create_player(),
        'status': "playing"
    }
```

## Creating the Player

The `create_player` function consumes nothing and produces a `Player` (dictionary). Because players start off with nothing in a fixed location, this function is quite short:

```python
def create_player():
    return {
        'location': 'yard',
        'inventory': [],
    }
```

## Creating the Map

The `create_map` function consumes nothing and produces a dictionary mapping location names (strings) to `Location` dictionaries. You will need to have a key/value pair in your dictionary for every location in your diagram. Therefore, this function will be much bigger:

```python
def create_map():
    return {
        'yard': {
            'neighbors': ['entrance', 'woods'],
            'about': "There are many weeds, surrounding a big scary house.",
            'stuff': [],
        },
        'woods': {
            'neighbors': ['yard'],
            'about': "It is dark here. You are likely to be eaten by a grue.",
            'stuff': ["Grue", "key"]
        },
        'entrance': {
            'neighbors': ['yard', 'dining room', 'upstairs'],
            'about': "You see stairs, and what appears to be a dining room.",
            'stuff': []
        },
        'dining room': {
            'neighbors': ['entrance'],
            'about': "There appears to be old, rotting food on the table.",
            'stuff': ["rotting food"]
        },
        'upstairs': {
            'neighbors': ['entrance'],
            'about': "There is a locked door.",
            'stuff': ["locked door"]
        }
    }
```

## Testing

We need to test and document each of these functions in turn, to confirm that they work. Again, we could test for literal equality, or we could be strategic. Remember, though, the less you test the less confident you can be about what's causing a given error. When you ask for help, you will usually be asked, "How many tests did you write?"

```python
player = create_player()
# Use the built-in isinstance function to confirm that we made a dictionary
assert_equal(isinstance(player, dict), True)
# Does it have the right keys?
assert_equal(len(player.keys()), 2)
assert_equal("location" in player, True)
assert_equal(player['location'], 'yard')
assert_equal("inventory" in player, True)
assert_equal(player['inventory'], [])

world = create_world()
# Is the world a dictionary?
assert_equal(isinstance(world, dict), True)
# Does the dictionary have the right keys?
assert_equal("status" in world)
assert_equal("map" in world)
assert_equal("player" in world)
# Is the world's status initially playing?
assert_equal(world['status'], 'playing')
# Did we use the create_map function correctly?
assert_equal(world['map'], create_map())
# Is the map a dictionary?
assert_equal(isinstance(world['map'], dict), True)

# ...
```

Next up: [Rendering the World](LINK)

# Rendering the World

The word "rendering" usually means drawing, but in a Text Adventure game it means writing text. The `render` function consumes a `World` and produces a string that can be shown to the player to describe the world. Note that we are producing a string, not printing anything - your code should not print!

The requirements about what to render are not strict, but there are some conventions. You will want to let the user know their current location, their current status, and give them some idea of their inventory. You should describe their current location, and possibly give them some hints about what they can do there.

## Decomposing Render

As with `create_world`, the `render` function has a lot to do. It makes sense to
break up the work with helper functions. We'll create three helper functions and
then combine their results.

```python
def render(world):
    return (render_location(world) +
            render_player(world) +
            render_visible_stuff(world))
```

Let's take a look at writing that first `render_location` funtion, which has
the same signature as `render` - it consumes a `World` and produces a string.

## Reading the World

Before you can describe the world, you need to access information about it.
Since the world is a dictionary, you will need to use dictionary lookup.
Because you will need to write a lot of logic involving many pieces of world state,
it is usually a good idea to use temporary variables:

```python
def render_location(world):
    # ...
    location = world['player']['location']
    here = world['map'][location]
    about = here['about']
    # ...
```

We can access the player's location using regular dictionary access. However,
getting information about that location (e.g., what stuff there is) is trickier
and requires using the World's map and the player's location name. From there,
however, it is easy to get data about the location we are in (`here`).

## Rendering Location

So what should we write about the current location? Again, we are in charge of
our game's design, so we could technically have it return whatever we want.

```python
def render_location(world):
    # ...
    return "Everything is in darkness. You see nothing."
```

But that's probably not very fun for the player. Instead, we'll identify the
current location and then describe it.

```python
def render_location(world):
    # ...
    return ("You are in "+location+"\n"+
            about+"\n")
```

## Dynamic Worlds

Remember, your world does not have to be static. You can hide items from the player's sight, or require them to have another item before they see something, or have things appear over the course of the game. In the Red Dot Quest, for instance, the World has a timer that increments after every round; certain items (like Catnip) are only visible during the day (when the timer is an even number). You are in control of the story.

`if` statements will allow you to have different renderings depending on the world's current state.
For example, in the Spooky House game, we could have hidden the Grue if the player has a flashlight (Grues prefer darkness). There are many ways to accomplish this, but one strategy is to create a copy of the stuff list that only includes the `"Grue"` string IF the value `"flashlight"` is not in the player's inventory.

```python
def render_visible_stuff(world):
    location = world['player']['location']
    here = world['map'][location]
    stuff = here['stuff']
    inventory = world['player']['inventory']
    
    visible_stuff = []
    for thing in stuff:
        if thing == 'Grue':
            if 'flashlight' not in inventory:
                visible_stuff.append(thing)
        else:
            visible_stuff.append(thing)
    
    return "You see: " + ', '.join(visible_stuff)
```

Be very careful about the mutability of the lists. You should be careful NOT to modify the world's `stuff` or the player's `inventory` from within this function (render functions should not modify the world, just draw it). Notice how the code above builds a new list instead of modifying the original!

## Testing

The `create_world` and `render_introduction` functions always produce the same value, because they have no parameters and do not take user input. Testing them was very straightforward. The `render` function, however, takes a `World`. Therefore, we will want to test that the rendering works for many kinds of worlds. Again, you can test either literal strings or be strategic and confirm that parts are correct.

```python
world = create_world()
assert_equal(render(world), """You are in yard.
There are many weeds, surrounding a big scary house.
You can see nothing.
You have nothing.""")

world['player']['location'] = 'woods'
assert_equal("Grue" in render(world), True)

world['player']['inventory'].append('flashlight')
assert_equal("Grue" in render(world), False)
assert_equal("flashlight" in render(world), True)
```

Next up: [Getting Options](LINK)

# Getting Options

You determine the next commands available to the player by implementing `get_options`, which consumes a `World` and produces a list of strings. Each string should be a valid option for the player to choose.

According to the project rules, every game needs to support the Quit option, so we'll want to start there.

```python
def get_options(world):
    # ...
    commands = ["Quit"]
    # ...
    # Add more commands
    # ...
    return commands
```

From there, we will probably want to add commands for moving between locations (e.g., `"Go to nearby forest"`), for picking up stuff in the world (e.g., `"Get key"`), and for using items in your inventory (e.g., `"Use flashlight"`). When data is in lists, you can take advantage of `for` loops to iterate through and build up the result. If options should only be available in certain locations, you'll need `if` statements. Similar to `render`, you should use functional decomposition to break up `get_options`. Because lists are mutable, you should be conscious of how the data gets passed around.

Next up: [Updating the World](LINK)

# Updating the World

Our next command to implement is `update`, which consumes a `World` and a command (a string) and produces a string that describes any changes that are made. This function is very unusual because it has *side-effects*. You are intentionally going to modify the World dictionary that was passed in.

This should be the only function that modifies the `World` directly. Logically, the other functions are only creating and reading the World, not manipulating it. Let's make a basic `update` that only supports one command: "Quit".

```python
def update(world, command):
    
    if command == "quit":
        world['status'] = 'quit'
        return "You quit the game"
    
    return "Unknown command: "+command
```

## Handling Many Options

Obviously, our Spooky House game has to support more than just the `"quit"` option.
We could hardcode all of our commands:

```python
if command == "eat food":
    world['status'] = 'lost'
elif command == "use key":
    ...
```

However, this will become tedious and error-prone if we do all our commands this way.
Instead, we can use clever conditionals to combine related functionality.
We'll also move the code to a new function to help keep the complexity down.

```python
def goto(world, command):
    new_location = command[len('go to '):]
    world['player']['location'] = new_location
    return "You went to "+new_location

def update(world, command):
    if command.startswith('go to '):
        return goto(world, command)
    ...
```

## World Mutability

The `World` is a dictionary, and has a number of lists and dictionaries inside of it. Recall that these types are *mutable*, which means that modifications (e.g., updating the value associated with a key or using `append`) will modify without producing a changed one. If you write a function that deletes an element from a list, that element is now gone from the world even in other functions.

You will frequently encounter issues where you find that your World was updated in ways you didn't anticipate. It is essential that you keep track of what parts of your code manipulate your data. Testing will help substantially.

Next up: [Rendering the Ending](LINK)

# Rendering the Ending

The `render_ending` function consumes a `World` and produces a string describing the ending for your game. There are three potential ending statuses: `"won"`, `"lost"`, and `"quit"`. Your only requirement is to have a different message for each of the three endings.

```python
def render_ending(world):
    if world['status'] == 'won':
        return "You won!"
    elif world['status'] == 'lost':
        return "You lost."
    elif world['status'] == 'quit':
        return "You quit."
```

Beyond that, you are free to have whatever message you want. In fact, you might even have multiple endings depending on how you lost, or how you won, or even how you quit. For instance, the Spooky House game has two ways of losing. We might decompose the `render_ending` function with a `render_ending_lost` helper function that looks like:

```python
def render_ending_lost(world):
    if 'food' in world['player']['inventory']:
        return ("You ate the gross, squishy food.\n"+
                "You got sick and collapsed.\n"+
                "You lose!")
    else:
        return ("You were eaten by a Grue.\n"+
                "You lose!")
```

Next up: [Integration Testing](LINK)

# Integration Testing

Once we have a basic definition for all of our commands, we can move beyond unit tests (which confirm individual functions) and into *integration testing* (which confirms the functions play well with each other). The idea is to simulate the game engine's execution and write assertions after each phase.

```python
def play_round(world, command):
    text = ""
    text += render(world)
    options = get_options(world)
    assert_equal(command in options, True)
    text += update(world, command)
    return text

world = create_world()
assert_equal(play_round(world, "go to woods"), """You are in yard.
There are many weeds, surrounding a big scary house.
You see nothing.
You have nothing.
You go to woods.""")

assert_equal(play_round(world, "check grue"), """You are in woods.
It is dark. You are likely to be eaten by a grue.
You see: key.
You have nothing.
You check the grue."""

assert_equal(world['status'], 'lost')
```

You can add many more assertions to the above to improve the validity. You might also find it helpful to write a helper function to test that your world is in a valid state.

```python
def test_world(world):
    assert_equal(isinstance(world, dict), True)
    assert_equal(len(world.keys()), 3)
    assert_equal("status" in world)
    ...
```

The `WIN_PATH` and `LOSE_PATH` variables that you are required to make might be good starting points for your functions.

```python
LOSE_PATH = ["enter house", "dining room", "eat food"]

# ...

world = create_world()
for command in LOSE_PATH:
    play_round(world, command)
assert_equal(world['status'], 'lost')
```

## Code Coverage

As you test your game, you will want to check your code coverage.
Your coverage indicates how much of your code you have tested.
You should aim to get 100% code coverage, although this does not mean that your game is correct.
Read up on [Code Coverage](LINK).

Next up: [Advanced Ideas](LINK)

# Advanced Ideas

Here are a few advanced ideas if your game is coming along.

## Case-Insensitive Input

Users often forget to capitalize their commands while typing. Making your game *case-insensitive* means that it will work the same regardless of whether or not users use the right capitalization. This can be accomplished by modifying your game functions and incorporating the `.lower()` method strategically.

## Encounters

In the Red Dot Quest, you could encounter several things (two allies and an enemy). During an encounter, the usual world map options are replaced with battle commands. This kind of system is actually surprisingly easy to make, simply by decomposing your core game functions appropriately:

```python
def render(world):
    if world['encounter']:
        return render_encounter(world)
    else:
        return render_overworld(world)
```

From here, you can implement two different versions of your game: `render_encounter` and `render_overworld`, allowing you to mentally isolate the different behavior. The same idea extends to `update` and `get_options`.

Note the careful use of `return` here. If you neglect to return the result of the called functions, their result is tossed away instead of being returned from `render`.

## Function Dispatch

We have encouraged the use of big `if/elif` chains in your functions. However, these are typically error-prone: lot's of repeated code is likely to let you make a syntactical or semantical error. Instead, you can often accomplish the same idea using a Lookup dictionary and function values:

```python
def goto(world, command):
    ...

def collect(world, command):
    ...

COMMAND_MAP = {
    'goto': goto,
    'collect': collect,
}

def update(world, command):
    verb = command[:command.find(' ')]
    action = COMMAND_MAP[verb]
    return action(world, command)
```

The `COMMAND_MAP` associates strings with functions. Notice that there are no parentheses after the function names, which means that they will not be called. Inside of `update`, the first line finds the verb portion of the `command` (the part before the first space), and then the second line looks up the relevant function in the `COMMAND_MAP`. The last line calls the function (stored in `action`) and passes in the `world` and `command`. This is known as "Function Dispatch".

## Ascii Art

Many early text adventure games took advantage of the medium by drawing graphics on the console using Ascii Art. You saw this earlier in the semester when you drew a Corgi using just text characters.

There are [collections of Ascii Art](https://www.asciiart.eu/), although you should be sure to cite anything that you use. 

Many early systems took advantage of [box-drawing characters](https://en.wikipedia.org/wiki/Box-drawing_character) that are available in Ascii.
