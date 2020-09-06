---
waltz:
  title: Reference- Code Cleanup with Black
  resource: page
  published: true
---
As software engineers, we often care about "Code Quality". While this covers a
number of ideas like functional decomposition, it also covers the way we break
up long lines and have whitespace around operators. This can be a small nit-
picky kind of thing, and we don't take off tons of points for it. One of the
reasons for this is because there are often tools for automatically cleaning
up code.

"Black" is one of these tools. Its name comes from an old quote by Henry Ford:
"[You can have any color you want, as long as its
black](http://superinnovator.blogspot.com/2012/02/you-can-have-any-color-you-
want-so-long.html)". The concept here is that Black will reformat your code in
a completely uncompromising way that fits a pretty nice standard. So you can
organize your code however you want, as long as its black.

The name isn't really important, I just thought that was interesting.

### Using Black

You will need to install the Black package:

  * Click Tools-> Manage Packages
  * Type "black" without quotes and press "Find package from PyPi"
  * The "black" package should come up.
  * Click the Install button to install coverage.
  * The package will now install.
  * Click the Close button to dismiss the window.

Then, in your shell, you can run the following line:

```python

!black project_starter.py
```

Or the name of whatever file you want to have it reformat. Note that this will
change the file; you might want to make a back-up first.

Now, if someone says that your code is messy, you can say that you had
reformatted it using Black and we can't argue against that. Note that you will
still need to have good functional decomposition, variable names, etc.
Automated tools can only help so much.