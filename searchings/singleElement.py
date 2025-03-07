def singleNonDuplicate(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
        
    for num, count in freq.items():
        if count == 1:
            return num
print(singleNonDuplicate([1,2,2,2,2,3,2,0,3]))
