def is_palindrome(sub):
    return sub == sub[::-1]

def longest_palindrome(s):
    max_len = 0
    result = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j+1]
            if is_palindrome(sub_string) and len(sub_string) > max_len:
                max_len = len(sub_string)
                result = sub_string

    return result
print(longest_palindrome("babad"))  # Output: "bab" or "aba"
print(longest_palindrome("cbbd"))   # Output: "bb"
