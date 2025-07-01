def longest_common_prefix(strs):
    if not strs:
        return strs
    res=''
    for i in range(len(strs[0])):
        char=strs[0][i]
        for word in strs:
            if i>=len(word) or word[i]!=char:
                return res
        res+=char
    return res
print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix(["dog","racecar","car"]))