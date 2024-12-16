# Kadane's Algorithm
# Difficulty: MediumAccuracy: 36.28%Submissions: 1MPoints: 4
# Given an integer array arr[]. You need to find the maximum sum of a subarray.

# Examples:

# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.
# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray {-2} has the largest sum -2.
# Input: arr[] = [5, 4, 1, 7, 8]
# Output: 25
# Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        res=arr[0]
        maxEnding=arr[0]
        for i in range(1,len(arr)):
            maxEnding=max(maxEnding+arr[i],arr[i])
            res=max(res,maxEnding)
        return res