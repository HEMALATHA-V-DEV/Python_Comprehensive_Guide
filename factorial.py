#Using Python’s Built-in math.factorial() Function: Python has a built-in function for calculating factorials. 

import math

number = 5
result = math.factorial(number)
print(f"The factorial of {number} is {result}")


# Define a function to calculate the factorial of a number - recursion
def factorial(n):
    # Base case: if n is 0, return 1 (as 0! = 1)
    if n == 0:
        return 1
    # Recursive case: multiply n by the factorial of n-1
    else:
        return n * factorial(n-1)  # Corrected typo here

# Test the function with a number
number = 5

# Call the factorial function and store the result
result = factorial(number)

# Print the result
print(f"The factorial of {number} is {result}")
