def sorting_sentence(s):
    s=s.split()
    keys=[]
    values=[]
    for word in s:
        for i in range(len(word)):
            if word[i].isdigit():
                keys.append(int(word[i]))
                values.append(word[:i]+word[i+1:])
    combined=sorted(zip(keys,values))
    result=[]
    for pair in combined:
        result.append(pair[1])
    result=" ".join(result)
    return result
print(sorting_sentence("is2 sentence4 This1 a3"))
print(sorting_sentence("Myself2 Me1 I4 and3"))
