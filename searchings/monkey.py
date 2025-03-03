# //Koko eating banana
import math
def findingMinSpeed(piles,H):
    left=0
    right=max(piles)
    while left<right:
        mid=(left+right)//2
        hours=0
        for pile in piles:
            hours+=math.ceil(pile/mid)
        if hours>H:
            left=mid+1
        else:
            right=mid
    return left
# print(findingMinSpeed([3,2,1,4,2,6],8))
print(findingMinSpeed([3,4,2,6,8],8))


# finding the target in an sorted rotated array

def search_in_rotated_array(arr, target):
    low, high = 0, len(arr) - 1  # Initialize the search range

    while low <= high:  # Perform binary search
        mid = (low + high) // 2  # Calculate the middle index

        # If the middle element is the target, return its index
        if arr[mid] == target:
            return mid

        # Check if the left half [low to mid] is sorted
        if arr[low] <= arr[mid]:  
            # If target lies within the sorted left half, search in this half
            if arr[low] <= target < arr[mid]:  
                high = mid - 1  # Move the search range to the left half
            else:  # Otherwise, search in the right half
                low = mid + 1  

        # If the left half is not sorted, then the right half must be sorted
        else:
            # If target lies within the sorted right half, search in this half
            if arr[mid] < target <= arr[high]:  
                low = mid + 1  # Move the search range to the right half
            else:  # Otherwise, search in the left half
                high = mid - 1  

    return -1  # If target is not found, return -1

# Example usage:
arr = [10, 15, 20, 0, 5]  # Rotated sorted array
target = 5
print("Index of target:", search_in_rotated_array(arr, target))  # Expected output: 4
