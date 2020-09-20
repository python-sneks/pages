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

    A. **`def` Keyword**  
    B. **Function name**  
    C. **Open parentheses**: `(`  
    D. **Parameters**: Remember, each parameter needs to have:  
    
      1. **Parameter name**
      2. **Colon**: `:`
      3. **Parameter type**
      4. **Comma**: But only *between* parameters.
    
    E. **End parentheses**: `)`  
    F. **Arrow**: `->`  
    G. **Return type**  
    H. **Colon**: `:`  
    
2. **Write a Docstring**: Put a triple-quoted string literal(`""" Like this """`) inside of the function, indented with four spaces. Inside the literal, write a description of what the function does. Then unindent the next line to leave the function.
3. **Write a Unit Test**: Have you written at least one test case, including...

    A. **Calling `assert_equal` function**  
    B. **Calling your function**: Make sure you call the function you are testing as the first argument to `assert_equal`.  
    C. **Arguments**: Your test case's inputs are the arguments to your function.  
    D. **Expected Value**: The second argument to the `assert_equal` should be a value that you expect your function to return.  

4. **Make More Unit Tests**: Make several more test cases, trying to think about:  

    A. A simple case that gives an example of the function under normal circumstances  
    B. A case where integers are zero, strings are the empty string, or lists are empty  
    C. A more complex case using unusual numbers, symbols, or other values.  

5. **Body**: Now, you can think about what to put in the body, making sure you end with...  
    A. **Return Statement**: If your function does not use the `return` statement with a value, then it will return `None`.
