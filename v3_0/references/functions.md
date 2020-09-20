---
waltz:
  title: Reference- Functions
  resource: page
  published: true
---

# Defining Functions Checklist

When you are struggling to define a function, it helps to have a plan. You might want to print this page out and keep it by your side.

Write the parts of the function in this order:

1. **Function Header**: Have you written the header, including...

    1.1. **`def` Keyword**
    
    1.2. **Function name**
    
    1.3. **Open parentheses**: `(`
    
    1.4. **Parameters**: Remember, each parameter needs to have:
    
        a. **Parameter name**
        
        b. **Colon**: `:`
        
        c. **Parameter type**
        
        d. **Comma**: But only *between* parameters.
    
    1.5. **End parentheses**: `)`
    
    1.6. **Arrow**: `->`
    
    1.7. **Return type**
    
    1.8. **Colon**: `:`
    
2. **Write a Docstring**: Put a triple-quoted string literal(`""" Like this """`) inside of the function, indented with four spaces. Inside the literal, write a description of what the function does. Then unindent the next line to leave the function.
3. **Write a Unit Test**: Have you written at least one test case, including...

    3.1. **Calling `assert_equal` function**
    3.2. **Calling your function**: Make sure you call the function you are testing as the first argument to `assert_equal`.
    3.3. **Arguments**: Your test case's inputs are the arguments to your function.
    3.4. **Expected Value**: The second argument to the `assert_equal` should be a value that you expect your function to return.

4. **Make More Unit Tests**: Make several more test cases, trying to think about:

    4.1. A simple case that gives an example of the function under normal circumstances
    4.2. A case where integers are zero, strings are the empty string, or lists are empty
    4.3. A more complex case using unusual numbers, symbols, or other values.

5. **Body**: Now, you can think about what to put in the body, making sure you end with...
    5.1. **Return Statement**: If your function does not use the `return` statement with a value, then it will return `None`.
