# Move All Zeroes to End
# Difficulty: EasyAccuracy: 45.51%Submissions: 255K+Points: 2
# Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.

# Examples:

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.
# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.
# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.
class Solution:
    def pushZerosToEnd(self,arr):
         non_zero = 0  
         for i in range(len(arr)):
            if arr[i] != 0: 
                arr[non_zero], arr[i] = arr[i], arr[non_zero]  
                non_zero += 1  

         return arr