from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Convert the dictionary into a list of tuples (num, frequency)
        freq_items = list(freq.items())

        # Step 3: Apply Selection Sort to sort elements by frequency in descending order
        n = len(freq_items)
        for i in range(n):
            max_index = i  # Assume the first element is the largest in the unsorted part
            for j in range(i + 1, n):
                if freq_items[j][1] > freq_items[max_index][1]:  # Compare frequencies
                    max_index = j
            # Swap the most frequent element to the correct position
            freq_items[i], freq_items[max_index] = freq_items[max_index], freq_items[i]

        # Step 4: Extract the top k elements from the sorted list
        result = []
        for i in range(k):
            result.append(freq_items[i][0])

        return result
