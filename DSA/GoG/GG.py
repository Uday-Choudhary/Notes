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

# Day3
# class Solution:
#     def reverseArray(self, arr):
#         i = 0
#         j = len(arr) - 1
#         temp = -1
#         while (i <= j):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#             i += 1
#             j -= 1
#         return arr

# Day4
# User function Template for python3

from typing import List


class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n
        pos = 0
        stored_part = []
        for i in range(d):
            stored_part.append(arr[i])

        for i in range(d, n):
            arr[pos] = arr[i]
            pos += 1

        for i in range(d):
            arr[pos] = stored_part[i]
            pos += 1

        return arr


# Day 7
class Solution:
    def maximumProfit(self, prices) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

#Day 8
#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        n = len(arr)
        arr.sort()
        initial_diff = arr[-1] - arr[0]
        smallest = arr[0] + k
        largest = arr[-1] - k
        min_diff = initial_diff
        
        for i in range(n-1):
            min_elem = min(smallest , arr[i+1] - k)
            max_elem = max(largest, arr[i] + k)
            
            if min_elem < 0:
                continue
            min_diff = min(min_diff , max_elem - min_elem)
        return min_diff
