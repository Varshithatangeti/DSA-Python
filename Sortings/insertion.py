arr=[3,4,25,6,990,2]
n=len(arr)
for i in range(0,n):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break
print("Sorted array is:",arr)

# arr = [3, 4, 25, 6, 990, 2]  # Input array
# n = len(arr)  # Length of the array

# # Outer loop: Iterate through the array starting from the first element
# for i in range(0, n):
#     # Inner loop: Compare the current element with the elements in the sorted portion
#     for j in range(i, 0, -1):  # Move backward from the current index `i` to `0`
#         if arr[j] < arr[j - 1]:  # Check if the current element is smaller than the previous one
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Swap the elements
#         else:
#             break  # Exit the inner loop if no further swaps are needed

# # Print the sorted array after all iterations
# print("Sorted array is:", arr)
