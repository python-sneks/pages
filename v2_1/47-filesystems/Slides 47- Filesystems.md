
[Download slides](https://udel.instructure.com/files/76109834/download){: .instructure_file_link .instructure_scribd_file }


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/JRDz5Jn4W8E?feature=oembed&amp;rel=0" 
></iframe>


#### Files

Your computer is equipped with a filesystem that lets you save and load files.
A file is simply a sequence of data, not unlike a string.
You create files all the time - text documents, pictures, music, python files, and so on.
These files are organized by your File System.

> A picture modeling someone's file system. At the top is a folder labeled "root", with three arrows pointing downwards at three other folders.  
> The first folder is labeled "School work" and has two files below (a word document and a excel spreadsheet).  
> The second folder is labeled "Photos" and has two picture files in it.  
> The third folder is labeled "Python" and has two Python files in it.

#### Directories

Directories, also known as folders, are a way to group files and other directories together.
Because we can put directories inside of directories, we end up with a hierarchical system.

> "Directories" are "Folders"

#### Paths

Think of files as a house.
Directories are neighborhoods, cities, states, and successively bigger ways to group houses.
Each file has a unique address within your file system called its "path".
We use these paths to navigate files and directories, just like we would houses and neighborhoods.

> The model from before, with three layers of files and folders, is shown.  
> A blue line traces a route from the Root down to one of the Python files with the label "path" on it.

#### Absolute Path

The full address for a file is known as its "absolute path".
The exact format of the path will depend on your platform, but typically they are a series of folder names separated by slashes. 
In Python, it is typically best to use forward slashes, since these tend to work regardless of the platform.

> Three example possible paths are shown.  
> Depending on your operating system, paths on your computer might look more or less like these.

```
/root/python/example.py
/home/acbart/python/example.py
C:/Users/acbart/python/example.py
```

#### The Working Directory

Most modern programming environments, like Thonny, have a command line that let you interact with the file system.
These command lines have a **Current Working Directory**.
It's essentially "where you are" at the moment.
In Thonny, you can check your current directory using the `pwd` command with an exclamation mark in front of it.
PWD stands for Print Working Directory.
Note that this only only works in the command line, it's not actually a Python command.

```
>>> !pwd
'C:/Users/acbart/projects/pythonmisc'
```

#### Relative Paths

If there are folders in your current working directory, you can reference them without writing the Absolute Path.
Instead, the folder's path is simply it's name.
You can see a list of the folders in your current directory by using the `ls` command.
LS stands for "list", as in "list the files".

```
>>> !ls

Date        Time        Type  Size     Name
09/17/2017  09:41 PM    <DIR>          .
09/17/2017  09:41 PM    <DIR>          ..
09/12/2017  03:11 PM    <DIR>          photos
09/14/2017  05:34 PM    <DIR>          music
09/11/2017  02:45 PM    <DIR>          python
09/02/2016  06:08 PM             6,228 homework5.pdf
09/02/2016  06:08 PM             9,650 example.py
08/08/2015  07:43 PM           340,489 historyOfDogs.png
08/08/2015  07:44 PM           422,316 taxReturns.docx
```

#### Moving between directories

To move from one directory to another, we use the `cd` command.
You can move to an absolute path or a relative path.
You can also move up a folder level by using a pair of periods.

> Move to specific folder anywhere in your file system (absolute path)

```
>>> cd /c/Users/acbart/projects
```

> Move to folder in current directory (relative path)

```
>>> cd pythonmisc/
```

> Move up a level

```
>>> cd ../
```

#### Commands

It can be tricky to remember these commands, but knowing how to use them will serve you well when you start working on larger projects.

| Command | Description |
|------------|-----------------------------------------|
| !pwd | Print current working directory |
| !ls | List files in current working directory |
| !ls "path" | List files in the directory of the path |
| !cd "path" | Change the current working directory |
