# def selection_sort(arr):
#     # Get the length of the array
#     n = len(arr)

#     # Traverse through all array elements
#     for i in range(n):
#         # Assume the first unsorted element is the minimum
#         min_index = i
        
#         # Inner loop to find the minimum element in the unsorted portion of the array
#         for j in range(i + 1, n):
#             # Compare current element with the current minimum
#             if arr[j] < arr[min_index]:
#                 # Update min_index if a smaller element is found
#                 min_index = j

#         # After finding the minimum element, swap it with the element at index 'i'
#         # (if min_index has changed)
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#         # At this point, the element at index 'i' is in its correct sorted position

# # Example usage:
# arr = [29, 10, 14, 37, 13]

# # Call the selection_sort function
# selection_sort(arr)

# # Print the sorted array
# print("Sorted array:", arr)

array = [23, 32, 21, 43, 53]
n = len(array)

for i in range(n):
    min = i
    for j in range(i + 1, n):
        if array[j] < array[min]:
            min = j
    array[i], array[min] = array[min], array[i]

print("Sorted array:", array)

# array = [23, 32, 21, 43, 53]  # Input array
# n = len(array)  # Length of the array

# # Outer loop: Iterate through each element
# for i in range(n):
#     # Assume the current index `i` holds the smallest value in the unsorted part
#     min = i
#     # Inner loop: Find the index of the smallest element in the unsorted part
#     for j in range(i + 1, n):
#         if array[j] < array[min]:
#             min = j  # Update `min` with the index of the smallest element
#     # Swap the smallest element found with the element at index `i`
#     array[i], array[min] = array[min], array[i]

# # Print the sorted array
# print("Sorted array:", array)

