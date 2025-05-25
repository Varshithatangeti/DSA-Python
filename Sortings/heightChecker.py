from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)  # Use sorted to get a copy
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count
sol = Solution()
print(sol.heightChecker([1, 1, 4, 2, 1, 3]))  # Output: 3
