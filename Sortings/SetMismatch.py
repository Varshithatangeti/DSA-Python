from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        duplicate = -1
        for num in freq:
            if freq[num] > 1:
                duplicate = num
                res.append(duplicate)
                break

        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        missing = expected_sum - (actual_sum - duplicate)  # Adjusted for the duplicate
        res.append(missing)

        return res
sol = Solution()
print(sol.findErrorNums([1, 2, 2, 4]))  # Output: [2, 3]
