# Isaiah Lugo
# CSM III - Data Structures
# Week 10 - Palindrome Check

# Checks if a given string is a palindrome using the deque queue.
# A palindrome is a word, phrase, or sequence that reads the same backward as forward.
# This function preprocesses the input to ignore case and non-alphanumeric characters.
# from collections import deque

def is_palindrome(string):

    # Initialize a deque as a queue
    queue = deque()
    
    # Preprocess string - make lowercase, remove spaces and non-alphanumeric characters
    processed_string = ''.join(char.lower() for char in string if char.isalnum())
    
    # Add each character to the queue
    for char in processed_string:
        queue.append(char)

    # Check for palindrome by comparison
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True
# Main, function calling, input check, result output
if __name__ == "__main__":
    # Prompt user for a string input
    user_input = input("Enter a string to check if it's a palindrome: \n")
    
    # Check if the input string is a palindrome
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

