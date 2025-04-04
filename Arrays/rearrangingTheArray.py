def rearrangeArray(nums):
    # Step 1: Separate positive and negative numbers
    positives = []
    negatives = []
    
    for num in nums:
        if num > 0:
            positives.append(num)
        else:
            negatives.append(num)
    
    # Step 2: Merge using index-based iteration
    result = []
    for i in range(len(positives)):  # Since both lists are of equal length
        result.append(positives[i])  # Add one positive number
        result.append(negatives[i])  # Add one negative number
    
    return result

# Example usage:
nums = [3, 1, -2, -5, 2, -4]
print(rearrangeArray(nums))  # Output: [3, -2, 1, -5, 2, -4]
