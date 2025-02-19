# def guessNumber(n):
#     left=1
#     right=n
#     while left<=right:
#         mid=(left+right)//2
#         if guess(mid)==0:
#             return mid
#         elif guess(mid)==-1:
#             right=mid-1
#         else:
#             left=mid+1
#     return -1

# finding the square root of a number using binary search

def sqrt(n):
    left=0
    right=n
    while left<=right:
        mid=(left+right)//2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            left=mid+1
        else:
            right=mid-1
    return right
print(sqrt(4))