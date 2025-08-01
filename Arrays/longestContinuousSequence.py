def sequence(nums):
    count=0
    for i in range(len(nums)):
        temp=1
        for j in range(i+1,len(nums)):
            if nums[j]>nums[j-1]:
                temp+=1
            else:
                break
        if temp>count:
            count=temp
        
    return count
print(sequence([1,3,5,4,7]))
print(sequence([2,2,2,2]))