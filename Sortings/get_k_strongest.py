def get_k_strongest(arr, k):
    # Step 1: Sort the array to find the median
    arr.sort()
    
    # Step 2: Find the median
    median = arr[(len(arr) - 1) // 2]
    
    # Step 3: Define a custom sort function
    def custom_sort(x):
        # Sort by absolute difference from median, then by value
        return (abs(x - median), x)
    
    # Step 4: Sort the array using the custom sort function in descending order
    arr.sort(key=custom_sort, reverse=True)
    
    # Step 5: Return the top k strongest elements
    return arr[:k]

# Example usage
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8]
k = 3
print(get_k_strongest(arr, k))  # Output: [9, 1, 8]
