
def sortColors(nums):
    low, high, i = 0, len(nums) - 1, 0
        
    while i <= high:
        if nums[i] == 0:
            nums[i], nums[low] = nums[low], nums[i]
            low += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[high] = nums[high], nums[i]
            high -= 1
        else:
            i += 1
        return nums
print(sortColors([2,0,0,0,1]))
