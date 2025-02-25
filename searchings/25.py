def findPeakElement(nums):
        # Initialize search boundaries
    low = 0
    high = len(nums) - 1  # Last index of the array
        
        # Perform binary search
    while low < high:
        mid = (low + high) // 2  # Find the middle index
            
            # Compare the middle element with its next element
        if nums[mid] < nums[mid + 1]:  
                # If the right neighbor is greater, move towards the right half
            low = mid + 1
        else:
                # If mid is greater than or equal to its right neighbor, move left
            high = mid  

        # When the loop ends, 'low' will be at the peak index
    return low
