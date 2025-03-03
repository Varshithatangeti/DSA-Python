# //Koko eating banana
import math
def findingMinSpeed(piles,H):
    left=0
    right=max(piles)
    while left<right:
        mid=(left+right)//2
        hours=0
        for pile in piles:
            hours+=math.ceil(pile/mid)
        if hours>H:
            left=mid+1
        else:
            right=mid
    return left
# print(findingMinSpeed([3,2,1,4,2,6],8))
print(findingMinSpeed([3,4,2,6,8],8))