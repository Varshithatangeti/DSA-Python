# //Given an integer array arr[]. You need to find the maximum sum of a subarray.

# Examples:

# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.
def maxSubArraySum(self,arr):
        res=arr[0]
        maxEnding=arr[0]
        for i in range(1,len(arr)):
            maxEnding=max(maxEnding+arr[i],arr[i])
            res=max(res,maxEnding)
        return res