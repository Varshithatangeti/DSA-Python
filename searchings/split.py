def splitArray(nums,k):
    # Define the search space: 
    # The smallest possible sum is the maximum single element (min possible largest sum).
    # The largest possible sum is the sum of all elements (if we don't split).
    left, right = max(nums), sum(nums)

    # Helper function to check if we can split the array into `k` subarrays 
    # with a given maximum sum
    def canSplit(max_sum):
        subarrays = 1  # Start with one subarray
        current_sum = 0  # Running sum for the current subarray
        
        for num in nums:
            current_sum += num
            
            # If adding the current number exceeds max_sum, we start a new subarray
            if current_sum > max_sum:
                subarrays += 1  # Increase subarray count
                current_sum = num  # Start a new subarray with the current number
            
            # If the number of subarrays exceeds k, return False
            if subarrays > k:
                return False
        
        return True  # If we managed to split within k subarrays, return True

    # Apply binary search on the range [max(nums), sum(nums)]
    while left < right:
        mid = (left + right) // 2  # Middle of the search space
        
        if canSplit(mid):  
            right = mid  # If we can split, try for a smaller maximum sum
        else:
            left = mid + 1  # If we cannot split, increase the allowed max sum

    return left  # The minimum largest sum possible after binary search

# Example usage
nums = [7, 2, 5, 10, 8]
k = 2
print("The minimum largest sum for", k, "subarrays is:", splitArray(nums, k))
