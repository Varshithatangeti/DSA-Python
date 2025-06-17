def counting_negatives(grid):
    count=0
    for row in grid:
        for val in row:
            if val>0:
                count+=1
    return count
print(counting_negatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))