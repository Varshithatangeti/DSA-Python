# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
# Function to reverse the words in a string
def reverse_words(s):
    # Remove leading and trailing spaces, then split into words
    words = s.strip().split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed words with a single space and return
    return ' '.join(reversed_words)
print(reverse_words("  hello world  "))          # Output: "world hello"
print(reverse_words("a good   example"))         # Output: "example good a"
print(reverse_words("  the sky is blue  "))      # Output: "blue is sky the"
print(reverse_words("Python"))                   # Output: "Python"
print(reverse_words("   spaced    out   words ")) # Output: "words out spaced"
 