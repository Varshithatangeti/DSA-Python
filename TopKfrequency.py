
def topKFrequent(words ,k):
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    res=[]
    for i in range(k):
        res.append(sorted_items[i][0])
    return res
print(topKFrequent(["i","love","leetcode","i","love","coding"],2))
print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"],4))