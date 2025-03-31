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
# Description of the Code:
# The function smallerNumbersThanCurrent(nums) determines how many numbers in the list are smaller than each element.

# Step-by-Step Explanation:
# Create an empty list result to store the count of smaller numbers for each element.

# Loop through each element (num) in nums:

# Initialize a counter count = 0 to track how many numbers are smaller than num.

# Compare num with every other element (other) in nums:

# If other is smaller than num, increase count by 1.

# Store count in the result list.

# Return result as the final output.

