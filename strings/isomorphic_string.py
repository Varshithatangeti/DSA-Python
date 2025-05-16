def is_isomorphic(s, t):
    # If lengths are different, the strings can't be isomorphic
    if len(s) != len(t):
        return False

    # Create two dictionaries to store character mappings
    # mapping1: maps characters from s to t
    # mapping2: maps characters from t to s
    mapping1 = {}
    mapping2 = {}

    # Loop through each character in both strings
    for i in range(len(s)):
        ch1 = s[i]  # Character from s
        ch2 = t[i]  # Corresponding character from t

        # Check if ch1 has been mapped before in mapping1
        if ch1 in mapping1:
            # If it was mapped to a different character, return False
            if mapping1[ch1] != ch2:
                return False
        else:
            # Store the new mapping from ch1 to ch2
            mapping1[ch1] = ch2

        # Check if ch2 has been mapped before in mapping2
        if ch2 in mapping2:
            # If it was mapped to a different character, return False
            if mapping2[ch2] != ch1:
                return False
        else:
            # Store the new mapping from ch2 to ch1
            mapping2[ch2] = ch1

    # All checks passed, strings are isomorphic
    return True
print(is_isomorphic("egg", "add"))       # True
print(is_isomorphic("foo", "bar"))       # False
print(is_isomorphic("paper", "title"))   # True
print(is_isomorphic("ab", "aa"))         # False
print(is_isomorphic("", ""))             # True (empty strings)
print(is_isomorphic("abc", "def"))       # True
print(is_isomorphic("aab", "xxy"))       # True
print(is_isomorphic("aab", "xyz"))       # False