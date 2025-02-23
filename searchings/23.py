# def min_subarray_len(target, nums):
#     l = 0  # Left pointer of the sliding window
#     total = 0  # Current sum of the window
#     res = float("inf")  # Initialize result to a large value

#     for r in range(len(nums)):  # Right pointer expands the window
#         total += nums[r]  # Add the current element to the window

#         while total >= target:  # If sum meets or exceeds target
#             res = min(r - l + 1, res)  # Update minimum subarray length
#             total -= nums[l]  # Remove the leftmost element from the window
#             l += 1  # Shrink the window from the left side

#     return 0 if res == float("inf") else res  # Return 0 if no valid subarray found

# # Example Usage
# print(min_subarray_len(7, [2,3,1,2,4,3]))  # Output: 2
# print(min_subarray_len(4, [1,4,4]))        # Output: 1
# print(min_subarray_len(11, [1,1,1,1,1,1,1,1]))  # Output: 0






def kWeakestRows(mat,k):
    soldier_count = []  # List to store the number of soldiers and row index

    # Count the number of soldiers (1s) in each row and store with index
    for i in range(len(mat)):  
        count = sum(mat[i])  # Count the number of 1s in the row
        soldier_count.append((count, i))  # Store (soldier count, row index)

    # Sort rows by soldier count first, then by row index if counts are equal
    soldier_count.sort()  

    weakest_rows = []  # List to store indices of the k weakest rows

    # Extract the indices of the first k weakest rows
    for i in range(k):  
        weakest_rows.append(soldier_count[i][1])  

    return weakest_rows  # Return the k weakest row indices