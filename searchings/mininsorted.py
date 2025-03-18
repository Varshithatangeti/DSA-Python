def minimum_in_sorted(array):
    left = 0
    right = len(array) - 1
    
    while left < right:
        mid = (left + right) // 2
        if array[mid] > array[right]:
            left = mid + 1
        else:
            right = mid
    
    return array[left]

print(minimum_in_sorted([4, 5, 6, 1, 2, 3]))