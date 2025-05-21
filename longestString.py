def longest_palindrome(str):
    def palindrome(s):
        reversed_string = s[::-1]
        if reversed_string == s:
            return True
        else:
            return False

    res = []
    for i in range(len(str)):
        if palindrome(str[i]):
            length = len(str[i])
            res.append(length)

    if res:
        result = max(res)
    else:
        result = 0

    return result

print(longest_palindrome(["abc", "racecar", "level", "noon", "hello"]))
