# Function to check if 'word' is a subsequence of 's'
def is_subsequence(s, word):
    i, j = 0, 0  # Two pointers: 'i' for s, 'j' for word
    while i < len(s) and j < len(word):  
        if s[i] == word[j]:  # If characters match, move pointer 'j' in word
            j += 1
        i += 1  # Always move 'i' in 's'
    
    # If we reached the end of 'word', it is a valid subsequence
    return j == len(word)

# Function to find the longest word in 'dictionary' that can be formed from 's'
def find_longest_word(s, dictionary):
    longest_word = ""  # Variable to store the longest valid word found

    for word in dictionary:
        # Check if the current word is a subsequence of 's'
        if is_subsequence(s, word):  
            # If the current word is longer than the longest_word found so far
            if len(word) > len(longest_word):  
                longest_word = word  # Update the longest_word
            # If the current word is of the same length but lexicographically smaller
            elif len(word) == len(longest_word) and word < longest_word:
                longest_word = word  # Update to choose the lexicographically smaller word
    
    return longest_word  # Return the longest valid word found

# Example Usage
s = "abpcplea"  # Input string
dictionary = ["ale", "apple", "monkey", "plea"]  # List of words to check

# Call the function and print the result
print(find_longest_word(s, dictionary))  # Output: "apple"
