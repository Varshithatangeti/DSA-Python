def word_search(string,substring):
    start=0
    end=len(substring)
    count=0
    while(end<=len(string)):
        if (substring==string[start:end]):
            count+=1
        start+=1
        end+=1
    return count
print(word_search("ABCDCDC","CDC"))
