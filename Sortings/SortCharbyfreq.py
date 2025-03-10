def frequency_sort(s: str) -> str:
    # Step 1: Count the frequency of each character
    freq = {}
    for letter in s:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    # Step 2: Extract unique characters into a list
    keys = list(freq.keys())

    # Step 3: Sort characters based on their frequency (Descending Order) using manual sorting
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if freq[keys[i]] < freq[keys[j]]:  # Swap if out of order
                keys[i], keys[j] = keys[j], keys[i]

    # Step 4: Build the output string by repeating characters based on their frequency
    result = []
    for char in keys:
        result.append(char * freq[char])  # Append the character repeated its frequency times

    # Step 5: Convert the list to a string and return it
    return "".join(result)

# Example Runs
print(frequency_sort("tree"))  # Output: "eetr" or "eert"
print(frequency_sort("cccaaa"))  # Output: "cccaaa" or "aaaccc"
print(frequency_sort("Aabb"))  # Output: "bbAa" or "bbaA"
