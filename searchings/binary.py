# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2  # Find the middle index
#         if arr[mid] == target:
#             return mid  # Return the index where the target is found
#         elif arr[mid] < target:
#             low = mid + 1  # Ignore the left half
#         else:
#             high = mid - 1  # Ignore the right half

#     return -1  # Return -1 if the target is not found

# # Example usage:
# arr = [1, 3, 5, 7, 9, 11, 13]  # Sorted array
# target = 7
# result = binary_search(arr, target)

# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found")


# finding the target index in a sorted nums using the binary search algorithm
# def binarySearch(nums,target):
#     left=0
#     right=len(nums)-1
#     while left<=right:
#         mid=(left+right//2)
#         if nums[mid]==target:
#             return mid
#         elif nums[mid]<target:
#             left=mid+1
#         else:
#             right=mid-1
#     return -1
# print(binarySearch([1,2,3,4,5,6,7,8,9],5))

# Finding the common element in two sorted arrays
# from typing import List

# class Solution:
#     def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
#         i, j = 0, 0
        
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] == nums2[j]:  
#                 return nums1[i]
#             elif nums1[i] < nums2[j]:  
#                 i += 1  
#             else:
#                 j += 1  
        
#         return -1  

# maximum count of positive integer and negative integer 
# def maxmimum_count(nums):
#     positive_count=0
#     negative_count=0
#     for num in nums:
#         if num>0:
#             positive_count+=1
#         elif num<0:
#             negative_count+=1
#         return max(positive_count,negative_count)
# print(maximum_count([1,2,3,-1,-2,-3]))      

