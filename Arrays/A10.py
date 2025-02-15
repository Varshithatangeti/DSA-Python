# Majority Element II
# Difficulty: MediumAccuracy: 48.1%Submissions: 110K+Points: 4
# You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

# Note: The answer should be returned in an increasing format.

# Examples:

# Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
# Output: [5, 6]
# Explanation: 5 and 6 occur more n/3 times.
# Input: arr[] = [1, 2, 3, 4, 5]
# Output: []
# Explanation: no candidate occur more than n/3 times.
# Constraint:
# 1 <= arr.size() <= 106
# 0 <= arr[i] <= 109

class Solution:
    def findMajority(self,arr):
        n = len(arr)
        freq = {}
        res = []
    
        # find frequency of each number
        for ele in arr:
            freq[ele] = freq.get(ele, 0) + 1
    
        # Iterate over each key-value pair in the hash map
        for ele, cnt in freq.items():
            
            # Add the element to the result, if its frequency
            # is greater than floor(n/3)
            if cnt > n // 3:
                res.append(ele)
    
        if len(res) == 2 and res[0] > res[1]:
            res[0], res[1] = res[1], res[0]
        return res