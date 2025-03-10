def majorityElement(nums):
    freq = {}  # Dictionary to store the frequency of each number
    res = []   # List to store the majority elements

    # Count the frequency of each number in the list
    for num in nums:
        if num in freq:
            freq[num] += 1  # Increment count if number already exists
        else:
            freq[num] = 1  # Initialize count for new number

    # Find elements that appear more than n/3 times
    for num in freq:
        if freq[num] > len(nums) // 3:  # Check if count is greater than n/3
            res.append(num)  # Add to result if condition is met
    
    return res  # Return the list of majority elements
nums = [4, 4, 2, 4, 3, 3, 3, 3]
print(majorityElement(nums))
