def kthSmallestPrimeFactor(arr,k):
    res=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            res.append((arr[i]/arr[j],arr[i],arr[j]))
    res.sort()
    fraction=res[k-1]
    numerator=fraction[1]
    denominator=fraction[2]
    return [numerator,denominator]
print(kthSmallestPrimeFactor([1,2,3,5],3))
