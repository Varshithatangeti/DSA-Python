def productOfSequence(nums):
    res=[]
    for i in range(len(nums)):
        temp=nums[:i]+nums[i+1:]
        product=1
        for i in temp:
            product*=i
        res.append(product)
    return res
print(productOfSequence([1,2,3,4]))
