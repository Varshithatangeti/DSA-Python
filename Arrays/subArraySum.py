def smallestSubWithSum(x, arr):
    n = len(arr)
    min_len = n + 1  # Initialize min_len with a value greater than the array length

    # Iterate over all possible starting points of subarrays
    for i in range(n):
        # Iterate over all possible ending points for subarrays starting from index i
        for j in range(i + 1, n + 1):
            sub_array = arr[i:j]  # Get the subarray from index i to j-1
            if sum(sub_array) > x:  # Check if the sum of the subarray is greater than x
                min_len = min(min_len, len(sub_array))  # Update min_len if a smaller valid subarray is found
                break  # Stop further expansion from this starting point since we want the smallest

    # Return the minimum length if a valid subarray was found; otherwise, return 0
    if min_len != n + 1:
        return min_len
    else:
        return 0
print(smallestSubWithSum(51, [1, 4, 45, 6, 0, 19]))  # Output: 3
print(smallestSubWithSum(100, [1, 10, 5, 2, 7]))     # Output: 0
