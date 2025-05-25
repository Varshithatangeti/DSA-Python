from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()  # Sort the array first
        min_difference = float('inf')  # Initialize to a large value

        # First pass to find the minimum absolute difference
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_difference:
                min_difference = diff

        res = []

        # Second pass to collect all pairs with that minimum difference
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_difference:
                res.append([arr[i - 1], arr[i]])  # Use a list here

        return res
sol = Solution()
print(sol.minimumAbsDifference([4, 2, 1, 3]))  # Output: [[1, 2], [2, 3], [3, 4]]
