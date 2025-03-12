from typing import List

# Function to sort people based on their heights in descending order
def sort_people(names: List[str], heights: List[int]) -> List[str]:
    # Combine heights and names into a list of tuples
    people = list(zip(heights, names))
    
    # Sort the list based on heights in descending order
    people.sort(reverse=True)
    
    # Extract and return the sorted names
    result = []
    for person in people:
        result.append(person[1])
    return result

# Test cases
names1 = ["Mary", "John", "Emma"]
heights1 = [180, 165, 170]
print(sort_people(names1, heights1))  # Output: ['Mary', 'Emma', 'John']

names2 = ["Alice", "Bob", "Bob"]
heights2 = [155, 185, 150]
print(sort_people(names2, heights2))  # Output: ['Bob', 'Alice', 'Bob']