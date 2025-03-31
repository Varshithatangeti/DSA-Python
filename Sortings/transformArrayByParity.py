from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # Iterate through the list and modify elements
        for i in range(len(nums)):
            # If the number is even, replace it with 0
            if nums[i] % 2 == 0:
                nums[i] = 0
            # If the number is odd, replace it with 1
            else:
                nums[i] = 1
        
        # Return the sorted version of the transformed array
        return sorted(nums)
# The given code defines a class Solution with a method transformArray that modifies a list of integers based on the following rules:

# Even numbers are replaced with 0.

# Odd numbers are replaced with 1.

# The modified list is then sorted and returned.

# This ensures that all 0s appear before 1s in the final output.