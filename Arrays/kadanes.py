def max_subarray_sum(nums):
    # Initialize max_sum and current_sum with the first element of the array
    max_sum = nums[0]  
    current_sum = nums[0]  
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Choose whether to start a new subarray or extend the current one
        current_sum = max(nums[i], current_sum + nums[i])  
        
        # Update max_sum if the current subarray sum is greater
        max_sum = max(max_sum, current_sum)  
    
    # Return the maximum subarray sum found
    return max_sum
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))  # Output: 6





def max_subarray_sum(arr):
    n = len(arr)
    
    # Initialize max_sum to the smallest possible value
    max_sum = float('-inf')  
   
    for i in range(n):
        current_sum = 0  # Reset sum for new subarray
        
        for j in range(i, n):
            current_sum += arr[j]  # Add current element
            
            # Update max_sum
            max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
print(max_subarray_sum([-5, -2, -8, -1]))  # Output: -1 (correct)
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6 (correct)
