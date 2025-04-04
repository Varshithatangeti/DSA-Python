def rowWithMax1s(matrix, n, m):
    # Initialize variables to keep track of the maximum number of 1s
    # and the corresponding row index.
    cnt_max = 0     # Stores the highest count of 1s found so far
    index = -1      # Stores the index of the row with maximum 1s

    # Loop through each row of the matrix
    for i in range(n):
        # Count the number of 1s in the current row using sum()
        cnt_ones = sum(matrix[i])

        # If the current row has more 1s than the previous maximum,
        # update cnt_max and store the current row index
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i

    # Return the index of the row with the most 1s
    # If no 1s are found in any row, it returns -1
    return index
matrix = [
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
n = 3  # number of rows
m = 4  # number of columns

print(rowWithMax1s(matrix, n, m))  # Output: 1 (second row has 3 ones)
