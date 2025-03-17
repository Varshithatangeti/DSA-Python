def can_place_cows(stalls, cows, min_dist):
    """
    Function to check if we can place 'cows' in 'stalls'
    such that the minimum distance between any two cows is at least 'min_dist'.
    """
    count = 1  # Place the first cow in the first stall
    last_position = stalls[0]  # Store the position of the last placed cow

    # Iterate over the remaining stalls
    for i in range(1, len(stalls)):
        # Check if the current stall is at least 'min_dist' away from last placed cow
        if stalls[i] - last_position >= min_dist:
            count += 1  # Place the cow
            last_position = stalls[i]  # Update the last placed position

            # If all cows are placed, return True
            if count == cows:
                return True

    return False  # Not enough space to place all cows


def aggressive_cows(stalls, cows):
    """
    Function to find the largest minimum distance possible between cows.
    """
    stalls.sort()  # Step 1: Sort the stalls to apply binary search

    # Step 2: Define the binary search range
    left, right = 1, stalls[-1] - stalls[0]  # Min and max possible distances
    ans = 0  # Variable to store the best answer

    # Step 3: Binary Search on the answer
    while left <= right:
        mid = (left + right) // 2  # Find the middle distance
        
        if can_place_cows(stalls, cows, mid):  # Check if we can place cows with this min distance
            ans = mid  # Store the valid distance
            left = mid + 1  # Try to maximize the minimum distance
        else:
            right = mid - 1  # Reduce the search space if placement is not possible

    return ans  # Return the maximum minimum distance found


# Taking input from the user
N, C = map(int, input().split())  # Read the number of stalls and cows
stalls = list(map(int, input().split()))  # Read the stall positions

# Call the function and print the result
print(aggressive_cows([1,2,4,8,9], 4))
