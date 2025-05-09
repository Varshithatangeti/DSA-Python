def setZeroes(matrix):
    """
    Modify the given matrix in-place such that if an element is 0, 
    its entire row and column are set to 0.
    """
    m = len(matrix)  # Number of rows
    n = len(matrix[0])  # Number of columns
    
    row = [0] * m  # List to track rows that should be zeroed
    col = [0] * n  # List to track columns that should be zeroed
    
    # First pass: Identify rows and columns that need to be set to zero
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = 1  # Mark the row
                col[j] = 1  # Mark the column
    
    # Second pass: Set elements to zero based on row and column markers
    for i in range(m):
        for j in range(n):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0  # Set element to zero
    
    # Print the modified matrix
    for row in matrix:
        print(row)

# ✅ Correct function call
print(setZeroes([[1, 0, 1], [0, 1, 0], [0, 1, 1]]))
