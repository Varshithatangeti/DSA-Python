# Finding the target element in the 2D matrix using binary search

class Solution:
    def searchMatrix(matrix, target):
        # Get the number of rows (m) and columns (n)
        rows, cols = len(matrix), len(matrix[0])

        # Set up binary search boundaries (treat the matrix as a 1D sorted list)
        left, right = 0, rows * cols - 1  

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2  # Find the middle index in the virtual 1D array
            
            # Convert 1D index to 2D row and column
            row, col = mid // cols, mid % cols  
            
            # Check if the middle element is the target
            if matrix[row][col] == target:
                return True  # Target found, return True
            
            # If target is greater, search the right half
            elif matrix[row][col] < target:
                left = mid + 1  

            # If target is smaller, search the left half
            else:
                right = mid - 1  

        return False  # If target is not found, return False



# Finding the 2 sum in the sorted array using the binary search      
def twoSum(numbers, target):
    l=0
    r=len(numbers)-1
    while l<r:
        currentSum=numbers[l]+numbers[r]
        if currentSum>target:
            r-=1
        elif currentSum<target:
            l+=1
        else:
            return [l+1,r+1]
    return []
