# Function to find maximum product subarray
class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        
        # Initialize variables to track the current maximum, current minimum, and overall maximum product
        currMax = arr[0]
        currMin = arr[0]
        maxProd = arr[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, n):
            # Temporary variable to store the current maximum before updating currMax
            temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)
            
            # Update currMin using the previous currMax value
            currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)
            
            # Update currMax using the temporary variable
            currMax = temp
            
            # Update the overall maximum product
            maxProd = max(currMax, maxProd)
        
        return maxProd