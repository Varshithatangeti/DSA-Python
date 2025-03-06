def shipWithinDays(weights, D):
    # Lower bound: max package weight (minimum capacity needed)
    # Upper bound: sum of all weights (max capacity needed)
    low, high = max(weights), sum(weights)

    # Function to check if we can ship with a given capacity
    def canShip(capacity):
        days = 1  # Start with the first day
        current_weight = 0  # Weight of packages in the current day
        
        for weight in weights:
            if current_weight + weight > capacity:
                # If adding this package exceeds capacity, start a new day
                days += 1
                current_weight = 0
            current_weight += weight  # Load package into current shipment

        return days <= D  # Return True if we can ship within D days

    # Perform binary search on capacity
    while low < high:
        mid = (low + high) // 2  # Try mid as the ship capacity
        if canShip(mid):
            high = mid  # If it's possible, try a smaller capacity
        else:
            low = mid + 1  # Otherwise, increase capacity

    return low  # The minimum capacity required

# Example Usage
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5
print(shipWithinDays(weights, D))  # Output: 15
