# Maximum Product Subarray
# Difficulty: MediumAccuracy: 18.09%Submissions: 417K+Points: 4
# Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

# Note: It is guaranteed that the output fits in a 32-bit integer.

# Examples

# Input: arr[] = [-2, 6, -3, -10, 0, 2]
# Output: 180
# Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180.
# Input: arr[] = [-1, -3, -10, 0, 6]
# Output: 30
# Explanation: The subarray with maximum product is {-3, -10} with product = (-3) * (-10) = 30.
# Input: arr[] = [2, 3, 4] 
# Output: 24 
# Explanation: For an array with all positive elements, the result is product of all elements. 
#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		n=len(arr)
		currMax=arr[0]
		currMin=arr[0]
		maxProd=arr[0]
		for i in range(1,n):
		    temp=max(arr[i],arr[i]*currMax,arr[i]*currMin)
		    currMin=min(arr[i],arr[i]*currMax,arr[i]*currMin)
		    currMax=temp
		    maxProd=max(currMax,maxProd)
		return maxProd