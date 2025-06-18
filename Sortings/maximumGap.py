def maximum_gap(nums):
    difference=0
    if len(nums)<2:
        return 0
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            diff=abs(nums[i]-nums[j])
            max_diff=max(diff,difference)
    return max_diff
print(maximum_gap([3,6,9,1]))
            