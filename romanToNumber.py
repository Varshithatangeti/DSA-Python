def roman_to_number(string):
    roman={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    total=0
    for i in range(len(string)):
        if i<len(string)-1 and roman[string[i]]<roman[string[i+1]]:
            total-=roman[string[i]]
        else:
            total+=roman[string[i]]
    return total
print(roman_to_number("III"))
print(roman_to_number("MCMXCIV"))
print(roman_to_number("LVIII"))