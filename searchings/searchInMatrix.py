# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
 

# Example 1:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -109 <= target <= 109

class Solution:
    def searchMatrix(matrix,target) -> bool:
        n = len(matrix)          # Number of rows
        m = len(matrix[0])       # Number of columns

        # Traverse each element in the matrix
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True  # Return True if target is found

        return False  # Return False if target is not found after full search
matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
target = 9
print(Solution().searchMatrix(matrix, target))  # Output: True
