
def sortArrayByParityII(nums):
    evenIndex = 0  # Pointer to track the next correct position for an even number
    oddIndex = 1   # Pointer to track the next correct position for an odd number
    n = len(nums)  # Get the length of the array

    while evenIndex < n and oddIndex < n:
        # If the number at evenIndex is already even, move to the next even position
        if nums[evenIndex] % 2 == 0:  
            evenIndex += 2  
        # If the number at oddIndex is already odd, move to the next odd position
        elif nums[oddIndex] % 2 == 1:  
            oddIndex += 2  
        # If numbers are misplaced, swap them
        else:
            nums[evenIndex], nums[oddIndex] = nums[oddIndex], nums[evenIndex]
            evenIndex += 2  # Move to the next even position
            oddIndex += 2   # Move to the next odd position

    return nums  # Return the modified array with correct parity arrangement

# Example usage
nums = [4, 2, 5, 7]
print(sortArrayByParityII(nums))  # Output: [4, 5, 2, 7] (or other valid answers)
