---
waltz:
  title: Reference- Functions
  resource: page
  published: true
---

When you are struggling to define a function, it helps to have a plan. You might want to print this page out and keep it by your side.

Write the parts of the function in this order:

[ ] **Function Header**: Have you written the header, including...
    [ ] **`def` Keyword**
    [ ] **Function name**
    [ ] **Open parentheses**: `(`
    [ ] **Parameters**: Remember, each parameter needs to have:
        [ ] **Parameter name**
        [ ] **Colon**: `:`
        [ ] **Parameter type**
        [ ] **Comma**: But only *between* parameters.
    [ ] **End parentheses**: `)`
    [ ] **Arrow**: `->`
    [ ] **Return type**
    [ ] **Colon**: `:`
[ ] **Write a Docstring**: Put a triple-quoted string literal(`""" Like this """`) inside of the function, indented with four spaces. Inside the literal, write a description of what the function does. Then unindent the next line to leave the function.
[ ] **Write a Unit Test**: Have you written at least one test case, including...
    [ ] **Calling `assert_equal` function**
    [ ] **Calling your function**: Make sure you call the function you are testing as the first argument to `assert_equal`.
    [ ] **Arguments**: Your test case's inputs are the arguments to your function.
    [ ] **Expected Value**: The second argument to the `assert_equal` should be a value that you expect your function to return.
[ ] **Make More Unit Tests**: Make several more test cases, trying to think about:
    [ ] A simple case that gives an example of the function under normal circumstances
    [ ] A case where integers are zero, strings are the empty string, or lists are empty
    [ ] A more complex case using unusual numbers, symbols, or other values.
[ ] **Body**: Now, you can think about what to put in the body, making sure you end with...
    [ ] **Return Statement**: If your function does not use the `return` statement with a value, then it will return `None`.
