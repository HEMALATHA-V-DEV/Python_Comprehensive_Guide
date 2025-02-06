# Define a function to check if a string is a palindrome
def is_pallindrome(string):
    # Reverse the string using slicing (string[::-1])
    reverstring = string[::-1]
    
    # Return True if the original string is equal to the reversed string, otherwise return False
    return string == reverstring

# Define a string variable 'word' with the value 'madam'
word = "madam"

# Call the 'is_pallindrome' function with 'word' as input
if is_pallindrome(word):
    # If the function returns True, print that the word is a palindrome
    print(f"{word} is a palindrome")
else:
    # If the function returns False, print that the word is not a palindrome
    print(f"{word} is not a palindrome")
