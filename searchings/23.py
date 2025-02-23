def min_subarray_len(target, nums):
    l = 0  # Left pointer of the sliding window
    total = 0  # Current sum of the window
    res = float("inf")  # Initialize result to a large value

    for r in range(len(nums)):  # Right pointer expands the window
        total += nums[r]  # Add the current element to the window

        while total >= target:  # If sum meets or exceeds target
            res = min(r - l + 1, res)  # Update minimum subarray length
            total -= nums[l]  # Remove the leftmost element from the window
            l += 1  # Shrink the window from the left side

    return 0 if res == float("inf") else res  # Return 0 if no valid subarray found

# Example Usage
print(min_subarray_len(7, [2,3,1,2,4,3]))  # Output: 2
print(min_subarray_len(4, [1,4,4]))        # Output: 1
print(min_subarray_len(11, [1,1,1,1,1,1,1,1]))  # Output: 0
