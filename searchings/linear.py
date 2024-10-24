def linear_search(array,target):
    for i in range(len(array)):
        if (i==target):
            return i
    return -1
array=[1,2,3,4,5]
target=1
result=linear_search(array,target)
if(result!=-1):
    print("The element found in the index",result)
else:
    print("The element is not found")