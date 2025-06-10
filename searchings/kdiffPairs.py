def kdiffPairs(nums, k):
    result = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                pair = tuple(sorted([nums[i], nums[j]]))  # fixed
                result.add(pair)  # fixed
    return len(result)

print(kdiffPairs([3, 1, 4, 1, 5], 2))  # fixed

