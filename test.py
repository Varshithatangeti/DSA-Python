
# finding max difference between two numbers in an array
def small(arr):
    differences = []
    for i in range(len(arr) - 1):  # avoid index error
        res = abs(arr[i] - arr[i+1])
        differences.append(res)
    return max(differences)
print(small([3, 2, 1, 9]))  # Output: 8