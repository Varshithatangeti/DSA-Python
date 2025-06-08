def numSubarrayProductLessThanK(nums,k):
    count=0
    for i in range(len(nums)):
        product=1
        for j in range(i,len(nums)):
            product*=nums[j]
            if product<k:
                count+=1
            else:
                break
    return count
print(numSubarrayProductLessThanK([10,5,2,6],100))