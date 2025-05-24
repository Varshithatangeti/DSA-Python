def findingDisappearedNumbers(nums):
    n=len(nums)
    full_set=set(range(1,n+1))
    actual_set=set(nums)
    return list(full_set-actual_set)
print(findingDisappearedNumbers([4,3,2,7,8,2,3,1]))
