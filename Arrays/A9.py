
# Explanation: The next permutation of the given array is {2, 4, 5, 0, 1, 7}.
# Input: arr = [3, 2, 1]
# Output: [1, 2, 3]
# Explanation: As arr[] is the last permutation, the next permutation is the lowest one.
# Input: arr = [3, 4, 2, 5, 1]
# Output: [3, 4, 5, 1, 2]
# Explanation: The next permutation of the given array is {3, 4, 5, 1, 2}.
class Solution:
    def nextPermutation(self, arr):
        # code here
        def reverse(arr,start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        pivot = float('-inf')
        n = len(arr)
        for i in range(n-1, -1,-1):
            if arr[i-1] < arr[i]:
                pivot = i-1
                break
        
        if pivot == -1:
            reverse(arr, 0, n-1)
        else:

        
            for i in range(n-1, pivot-1, -1):
                if arr[pivot] < arr[i]:
                    arr[pivot], arr[i] = arr[i], arr[pivot]
                    break
            reverse(arr, pivot+1, n-1)
        return arr