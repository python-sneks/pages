
[Download slides](File%20Formats.pdf)


<iframe style="width: 640px; height: 480px;" width="300" height="150" allowfullscreen="allowfullscreen" webkitallowfullscreen="webkitallowfullscreen" mozallowfullscreen="mozallowfullscreen"
title="Introduction.pdf"
src="https://www.youtube.com/embed/fRP5KVEjVJ4?feature=oembed&amp;rel=0" 
></iframe>


#### File Formats

When data is placed into a file, it often follows a regular structure.
That way, other users of the file can navigate the data more easily.
This structure is known as a file format.
Typically, a file's format is used to determine it's extension.
This is why Python files have a `".py"` at the end - even though they are text, they are structured according to the Python language.

> Three people are standing together, looking at a document.  
> The first one says "As you can see in this CSV file..." while another says "Ah yes, you're right, I see..."

#### Recall: Opening a File

Usually, regardless of the file format, we begin using it by opening the file.
Recall how we open text files using the open function, giving us a file object.
Previously, we then read the file directly.
Instead, we will now use special modules to read a file.

```python
data_file = open('filename.format')
```

> An annotation points out the use of the `open` function to read a "Path" stored in a string.

#### JSON Format

The JSON format is a particularly useful format, and is available in many programming languages.
The JSON format lets you store lists, dictionaries, and simple primitive types in a file.
When you load the data, you get the same structure back.
The example shown demonstrates how easy this is.
The `data` variable could now hold a complex nested structure of data, without having to embed it in the program.

```python
import json

json_file = open('data.json')

data = json.load(json_file)
```

#### Quickly Visualizing Data

Have a complex data structure, like a list of dictionaries?
Here's a quick pattern for easily visualizing the first element.
A very curious thing to note is second parameter for this function call.
This is known as a "keyword argument", and we have to explicitly give both the parameter and the argument.
The syntax is similar to an assignment, except all of it is embedded in the function call.

```python
print(json.dumps(data[0], indent=2))
```

> Prints out the following:

```
{
  "Name": "Klaus",
  "Age": 17,
  "Big?": true
}
```


#### CSV Format

Comma-Separated Values, or CSV, files are another very popular way to share data.
An advantage of CSV files is that they can be opened in programs like Excel, edited like text files, or processed in programming languages like Python.
To process a CSV File, you need to use the csv reader function, which can be a little complex.
This is a situation where referring to documentation and using Google is necessary.

```python
import csv

csv_file = open('data.csv')
for line in csv.reader(csv_file, delimiter=","):
    print(line)
```

#### Other Formats

There are many, many other file formats out there.
Some text formats are easy to process, but others require special libraries.
When encountering a new format, you should always check to see if there is a module available to load the data.

> A long list of format names are shown, including: `txt`, `json`, `csv`, `xml`, `log`, and many more.
