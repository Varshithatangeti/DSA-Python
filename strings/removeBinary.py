def remove_anagrams(words):
    res=[words[0]]
    for i in range(1,len(words)):
        if sorted(words[i])!=sorted(words[i-1]):
            res.append(words[i])
    return res
print(remove_anagrams(["abba","baba","bbaa","cd","cd"]))
print(remove_anagrams(["a","b","c","d","e"]))