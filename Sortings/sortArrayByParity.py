from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        This function sorts an array such that all even numbers appear first, 
        followed by odd numbers, while maintaining sorted order.
        """
        
        # Step 1: Sort the array in ascending order
        nums.sort()

        # Step 2: Create an empty list to store the result
        res = []

        # Step 3: Add all even numbers to the result list first
        for num in nums:
            if num % 2 == 0:  # Check if the number is even
                res.append(num)

        # Step 4: Add all odd numbers to the result list after evens
        for num in nums:
            if num % 2 != 0:  # Check if the number is odd
                res.append(num)

        # Step 5: Return the final list with evens first, then odds
        return res
