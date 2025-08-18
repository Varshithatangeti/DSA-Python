def valid_word(string):
    if len(string)<3:
        return False
    vowels="aeiouAeiou"
    has_vowels=False
    has_consonants=False
    for ch in string:
        if not(ch.isalpha() or ch.isdigit()):
            return False
        if ch in vowels:
            has_vowels=True
        elif ch.isalpha():
            has_consonants=True
    return has_vowels and has_consonants
print(valid_word("b3"))
print(valid_word("234Adas"))

