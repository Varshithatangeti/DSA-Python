def longest_substring(str):
    max_length=0
    for i in range(len(str)):
        for j in range(i,len(str)):
            substring=str[i:j+1]
            if len(set(substring))==len(substring):
                max_length=max(max_length,len(substring))
    return max_length
print(longest_substring("abcabcbb"))
print(longest_substring("bbbb"))
print(longest_substring("pwwkew"))