def kthSmallest(matrix,k):        
    arr = []
    
    for row in matrix:
        arr.extend(row)
    
    arr.sort()
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid == k - 1:
            return arr[mid]
        elif mid < k - 1:
            left = mid + 1
        else:
            right = mid - 1

matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print("The", k, "th smallest element is:", kthSmallest(matrix, k))