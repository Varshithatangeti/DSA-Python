# You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

# Note: Positive number starts from 1. The array can have negative integers too.

# Examples:

# Input: arr[] = [2, -3, 4, 1, 1, 7]
# Output: 3
# Explanation: Smallest positive missing number is 3.
# Input: arr[] = [5, 3, 2, 5, 1]
# Output: 4
# Explanation: Smallest positive missing number is 4.
# Input: arr[] = [-8, 0, -1, -4, -3]
# Output: 1
# Explanation: Smallest positive missing number is 1.
# Constraints:  
class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        arr.sort()
        res=1
        for num in arr:
            if num==res:
                res+=1
            elif num>res:
                break
        return res
# res will had the current smallest missing number...Initially set to 1
# if we have found res in the array
# res is no longer missing so increment it 
# if the current element is larger than result,res cannot be found in the array so it is our final answer