def kth_missing_positive_number(ls,k):
    res=[]
    Res=[]
    for i in range(1,1001):
        res.append(i)
    for i in res:
        if i not in ls:
            Res.append(i)
    return Res[k-1]
print(kth_missing_positive_number([2,3,4,7,11],5))