# Add Binary Strings
# Difficulty: MediumAccuracy: 23.25%Submissions: 88K+Points: 4
# Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
# Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

# Input: s1 = "1101", s2 = "111"
# Output: 10100
# Explanation:
#  1101
# + 111
# 10100
# Input: s1 = "00100", s2 = "010"
# Output: 110
# Explanation: 
#   100
# +  10
#   110
# Constraints:
# 1 ≤s1.size(), s2.size()≤ 106
class Solution:
	def addBinary(self, s1, s2):
		    result = bin(int(s1, 2) + int(s2, 2))[2:]
    return result
# This code defines a function called add_binary, which takes two binary strings, s1 and s2, as input and returns their sum as a binary string. Here’s a concise explanation of each part:

# Function Definition:

# def add_binary(s1, s2): defines the function named add_binary that accepts two parameters, s1 and s2, which are expected to be binary strings (like "1101" and "111").
# Conversion and Addition:

# int(s1, 2) converts the binary string s1 to an integer using base 2.
# int(s2, 2) does the same for s2.
# The two integers are added together.
# Back to Binary:

# bin(...)[2:] converts the resulting integer back to a binary string. The bin() function produces a string that starts with "0b", so [2:] slices off the "0b" part, leaving just the binary digits.
# Return Statement:

# The function returns the sum in binary format.
