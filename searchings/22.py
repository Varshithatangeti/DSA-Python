# # class Solution:
# def findMin(nums):  
#     left = 0  
#     right = len(nums) - 1  
        
#     while left < right:  
#         mid = (left + right) // 2  
#         if nums[mid] > nums[right]:  
#             left = mid + 1  
#         else:  
#             right = mid  
        
#     return nums[left]
# print(findMin([3,4,5,1,2]))

# finding the next greatest letter

# def nextGreatestLetter(letters,target):
#     left = 0
#     right = len(letters) - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if letters[mid] <= target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     if left == len(letters):
#         return letters[0]
#     return letters[left]
# print(nextGreatestLetter(['a','b','c','d','f'],'e'))