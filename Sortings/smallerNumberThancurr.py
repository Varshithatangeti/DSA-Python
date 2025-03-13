def smallerNumbersThanCurrent(nums):
    result = []  # List to store the count of smaller numbers for each element
    
    # Iterate through each number in the array
    for num in nums:
        count = 0  # Counter to keep track of numbers smaller than the current number
        
        # Compare the current number with every other number in the array
        for other in nums:
            if other < num:  # If the other number is smaller, increase the count
                count += 1
        
        result.append(count)  # Store the count in the result list
    
    return result  # Return the final list with counts

# Example usage
nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums))  # Output: [4, 0, 1, 1, 3]
