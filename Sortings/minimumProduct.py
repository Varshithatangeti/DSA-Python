
# Function to find the maximum product of (nums[i] - 1) * (nums[j] - 1)
def maxProduct(nums):
    product = 0  # Initialize a variable to store the maximum product
    
    # Iterate through the list to pick the first number
    for i in range(len(nums)):
        # Iterate through the list again to pick the second number, ensuring j > i to avoid duplicate pairs
        for j in range(i + 1, len(nums)):  
            # Calculate the product of (nums[i] - 1) and (nums[j] - 1)
            current_product = (nums[i] - 1) * (nums[j] - 1)
            
            # Update the maximum product if the current product is larger
            product = max(product, current_product)
    
    return product  # Return the highest product found

# Example usage
nums = [3, 4, 5, 2]
print(maxProduct(nums))  # Output: 12
