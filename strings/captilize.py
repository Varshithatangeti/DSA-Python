def solve(s):
    capitals = ''
    words = s.split(' ')
    for word in words:
        if len(word) > 0:
            if word[0].isalpha():
                res = word[0].upper() + word[1:]
            else:
                res = word
        else:
            res = ''
        capitals += res + ' '
    return capitals.strip()
print(solve("chris alan"))         # Output: Chris Alan
print(solve("12abc john"))         # Output: 12abc John
print(solve("  chris   alan  "))   # Output: Chris Alan
