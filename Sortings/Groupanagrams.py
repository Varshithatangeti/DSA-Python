from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Function to manually sort a string using a simple sorting method
        def manual_sort(s):
            s = list(s)  # Convert string to a list of characters
            n = len(s)
            # Selection sort to sort characters in ascending order
            for i in range(n):
                for j in range(i + 1, n):
                    if s[i] > s[j]:  # Swap if the current character is greater than the next
                        s[i], s[j] = s[j], s[i]
            return "".join(s)  # Convert sorted list back to a string

        # Dictionary to store grouped anagrams
        anagrams = {}

        # Iterate over each word in the input list
        for word in strs:
            sorted_word = manual_sort(word)  # Sort the word to get a common representation
            
            # If the sorted word exists, append the original word to its group
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:  # Otherwise, create a new list with the current word
                anagrams[sorted_word] = [word]

        # Convert dictionary values (list of anagram groups) into the final result list
        result = []
        for group in anagrams.values():
            result.append(group)

        return result  # Return the list of grouped anagrams
