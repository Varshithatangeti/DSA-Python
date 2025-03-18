def finding_kth_positive_missing(array, k):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        missing = array[mid] - (mid + 1)
        
        if missing < k:
            left = mid + 1
        else:
            right = mid - 1
    
    return left + k

print(finding_kth_positive_missing([2, 3, 4, 7, 11], 5))