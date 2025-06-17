def findTheDistanceValue(arr1,arr2,d):
    count=0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if abs(arr1[i]-arr2[j])<=d:
                break
        else:
            count+=1
    return count
print(findTheDistanceValue([4,5,8],[10,9,1,8],2))
print(findTheDistanceValue([1,4,2,3],[-4,-3,6,10,20,30],3))
print(findTheDistanceValue([2,1,100,3],[-5,-2,10,-3,7],6))