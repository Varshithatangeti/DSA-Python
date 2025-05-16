def largestOddNumber(num: str) -> str:
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[:i + 1]
    return ""  # Return empty string if no odd digit is found
print(largestOddNumber("52"))     # Output: "5"
print(largestOddNumber("4206"))   # Output: ""
print(largestOddNumber("35427"))  # Output: "35427"
print(largestOddNumber("123456")) # Output: "12345"
print(largestOddNumber("8888"))   # Output: ""
