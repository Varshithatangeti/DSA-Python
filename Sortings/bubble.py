# Implemetation of the BUBBLE SORTING
array=[1,4,3,5,8,2]
n=len(array)
for i in range(n-1):
    for j in range(n-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print('Sorted array:',array)


# # Implementation of Bubble Sort Algorithm

# # Initialize the array to be sorted
# array = [1, 4, 3, 5, 8, 2]

# # Get the length of the array
# n = len(array)

# # Outer loop: Traverse through all elements in the array
# # Runs n-1 times since the last element will already be sorted
# for i in range(n-1):
    
#     # Inner loop: Compare adjacent elements
#     # The range decreases as the largest elements "bubble up" to their correct positions
#     for j in range(n-i-1):
        
#         # If the current element is greater than the next element, swap them
#         if array[j] > array[j+1]:
#             array[j], array[j+1] = array[j+1], array[j]  # Swap operation

# # Print the sorted array
# print('Sorted array:', array)

