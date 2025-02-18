# Finding the lower boundary in an array using binary search
def lower_bound(arr,target):
    left,right=0,len(arr)
    while left<right:
        mid=(left+right)//2
        if arr[mid]<target:
            left=mid+1
        else:
            right=mid
    return left
print(lower_bound([1,2,2,2,3,4,5],2))




# Finding the higher bound in an array using the binary search
def higher_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

print(higher_bound([1, 2, 2, 2, 3, 4, 5], 2))