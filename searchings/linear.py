# Define the linear search function that takes an array and a target value as input
def linear_search(array, target):
    # Iterate through each index of the array
    for i in range(len(array)):
        # Check if the current element matches the target value
        if (array[i] == target):  # Fixed the condition to compare the element with the target
            return i  # Return the index of the found element
    return -1  # If the element is not found, return -1

# Define the array to search in
array = [1, 2, 3, 4, 5]

# Define the target value to search for
target = 1

# Call the linear_search function with the array and target
result = linear_search(array, target)

# Check if the element was found
if(result != -1):
    # If found, print the index where the element is located
    print("The element is found at index", result)
else:
    # If not found, print a message indicating the element was not found
    print("The element is not found")
