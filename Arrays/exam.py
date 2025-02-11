# # median of two sorted array
# # def median(arr):
# #     n=len(arr)
# #     for i in range(n):
# #         if n%2==0:
# #             return (arr[n//2]+arr[n//2-1])/2
# #         else:
# #             return arr[n//2]
# # print(median([1,2,3,4,5,6,7,8,9,10]))

# # def removing duplicates in an array
# def remove_duplicates(arr):
#     n=len(arr)
#     freq={}
#     for i in range(n):
#         if arr[i] in freq:
#             freq[arr[i]]+=1
#         else:
#             freq[arr[i]]=1
#     for i in range(len(freq)):
#         if freq[arr[i]]>1:
#             arr.remove(arr[i])
#     return arr
# print(remove_duplicates([1,1,2,3,4,3,2,1,2,1]))
