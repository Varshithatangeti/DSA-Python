from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Dictionary to store the frequency of each number
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1  # Increment frequency if number exists in dictionary
            else:
                freq[num] = 1  # Initialize frequency to 1 if number is not in dictionary

        # Sorting logic: Bubble Sort based on frequency and value
        for i in range(len(nums)):  # Outer loop iterates through the array
            for j in range(i + 1, len(nums)):  # Inner loop compares the current element with the next elements
                # Swap elements if:
                # 1. The frequency of nums[i] is greater than nums[j] (lower frequency should come first)
                # 2. If frequencies are equal, the larger number should come first
                if freq[nums[i]] > freq[nums[j]] or (freq[nums[i]] == freq[nums[j]] and nums[i] < nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]  # Swap the elements

        return nums  # Return the sorted array
