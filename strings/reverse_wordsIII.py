def reverese(s):
    s=s.split()
    reversed_words=[]
    for char in s:
        reversed_words.append(char[::-1])
    return " ".join(reversed_words)
print(reverese(" 'Let's take LeetCode contest' "))