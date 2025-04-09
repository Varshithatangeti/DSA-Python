def leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_from_right:
            max_from_right = arr[i]
            leaders.append(arr[i])
    leaders.reverse()  # Move this outside the loop
    return leaders  # Move this outside the loop

print(leaders([1, 6, 2, 4, 4, 5]))