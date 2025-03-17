import math  # Importing math module for the ceil function

def smallestDivisor(nums, threshold):
    # Helper function to compute the sum of elements when divided by divisor and rounded up
    def get_sum(divisor):
        total = 0  # Initialize sum
        for num in nums:
            total += math.ceil(num / divisor)  # Compute and add the ceiling division result
        return total  # Return the final sum

    # Setting the binary search range
    left, right = 1, max(nums)  # The divisor can be in the range [1, max(nums)]
    
    while left < right:  # Binary search loop
        mid = (left + right) // 2  # Find the middle divisor
        
        # Compute the sum of numbers when divided by mid and rounded up
        if get_sum(mid) > threshold:  
            # If the sum exceeds the threshold, we need a larger divisor
            left = mid + 1
        else:
            # If the sum is within the threshold, we try a smaller divisor
            right = mid
    
    return left  # When left == right, we have found the smallest valid divisor

# Example usage:
nums = [1, 2, 5, 9]  # Given array of numbers
threshold = 6  # Given threshold
print(smallestDivisor(nums, threshold))  # Output: 5
