from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Find the maximum number in the list
        maximum = max(nums)
        
        # Get the index of the maximum number
        max_index = nums.index(maximum)

        # Iterate through the list to check the "twice as large" condition
        for i in range(len(nums)):
            # Skip checking the maximum number itself
            if i != max_index:
                # If any number is more than half of the maximum, return -1
                if maximum < 2 * nums[i]:
                    return -1

        # If the condition holds for all elements, return the index of the maximum number
        return max_index
