---
waltz:
  title: Reference- Code Coverage
  resource: page
  published: true
---
Code coverage helps us answer the question, "Have I tested all of my code?"
Unfortunately, it is not a perfect system, but only a starting point. Still,
code coverage is a professional tool used daily by software engineers.

**Checking Coverage**

You will need to install the Python coverage package:

  * Click Tools-> Manage Packages
  * Type "coverage" without quotes and press "Find package from PyPi"
  * The "coverage" tool should come up.
  * Click the Install button to install coverage.
  * The package will now install.
  * Click the Close button to dismiss the window.

Now you can run the coverage command from the Shell at any time. You'll want
to replace the "ABCXYZ" part to the name of your game file and its test file.
Any extra Python files besides the main file and the tests should be added as
a comma-separated string after the --include parameter.

```python

>>> !coverage run ABCXYZ_tests.py
>>> !coverage html --include ABCXYZ.py,ABCXYZ_tests.py
```

To see the coverage report, use the appropriate command for your platform:

```python

# Windows
>>> !start htmlcov/index.html
# Mac
>>> !open htmlcov/index.html
# *Nix
>>> !xdg-open htmlcov/index.html
```

Click the name of a file to see what lines you have not run, highlighted in
red.

**How Much Coverage do I need?**

Do you need to get 100% coverage? Ideally. There are exceptions:

  * At the bottom of your main file, there's an IF statement with a comparison against `"__main__"`. You don't need to test this chunk of code.
  * Drawing functions (e.g., draw_world) are extremely difficult to test, you can't test them.
  * Function that only print and have no side effects are difficult to test; but you shouldn't need any of those for your final project.

You do not need to get code coverage on those functions in this course, though
you should know that it is technically possible!

If a function doesn't return anything and is not a drawing function, then it
is probably modifying the World dictionary. You still need to test these
functions. Check the tests from the example games for suggestions on how to do
so.