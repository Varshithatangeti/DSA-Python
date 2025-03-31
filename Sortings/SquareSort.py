from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums
# The given code defines a class `Solution` with a method `sortedSquares` that processes a list of integers as follows:  

# - **Squaring Elements:** It iterates through the list and replaces each element with its square.  
# - **Sorting the Squared Values:** It uses a nested loop (bubble sort) to sort the squared values in ascending order.  
# - **Returning the Result:** The sorted list of squared values is returned.  

# This approach has a **time complexity of O(n²)** due to the inefficient sorting method. A more optimal approach would be to use built-in sorting (`sorted(nums)`) or a two-pointer technique (**O(n log n) or O(n)** complexity).
