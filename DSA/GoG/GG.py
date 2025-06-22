# Day1
# class Solution:
#     def getSecondLargest(self, arr):
#         first = second = -1

#         for num in arr:
#             if num > first:
#                 second = first
#                 first = num
#             elif num != first and num > second:
#                 second = num

#         return second

# Day2
# class Solution:
# 	def pushZerosToEnd(self, arr):
#         pos = 0
#         for i in range(len(arr)):
#             if arr[i] != 0:
#                 arr[pos] = arr[i]
#                 pos+=1

#         for j in range(pos , len(arr)):
#             arr[j] = 0

#         return arr
