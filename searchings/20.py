# # finding the first and last position of element in sorted array
# from typing import List


# def searchRange(nums,target):
#     def findFirst(nums, target):
#         first = -1
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] >= target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#             if nums[mid] == target:
#                 first = mid
#             return first

#     def findLast(nums, target):
#             last = -1
#             left, right = 0, len(nums) - 1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] <= target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#                 if nums[mid] == target:
#                     last = mid
#             return last    

#     first = findFirst(nums, target)
#     last = findLast(nums, target)
#     return [first, last]
# print(searchRange([1,2,3,4,5,6,7,8,9],5))

# finding the sum of square numbers using binary search
# import math
# def judgeSquareSum(c):
#         left=0
#         right=int(math.sqrt(c))
#         while left<=right:
#             sumOfSquares=left*left+right*right
#             if sumOfSquares==c:
#                 return True
#             elif sumOfSquares<c:
#                 left+=1
#             else:
#                 right-=1
#         return False
# print(judgeSquareSum(25))