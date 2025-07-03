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
# Day10
# class Solution:
#     def maxSubArraySum(self, arr):
#         max_current = max_global = arr[0]
        
#         for i in range(1 , len(arr)):
#             max_current = max(arr[i] , max_current + arr[i])
#             max_global = max(max_global , max_current)
#         return max_global

# #Day11
# class Solution:
# 	def maxProduct(self,arr):
#         if not arr:
#             return 0
#         max_ending_here = min_ending_here = max_so_far = arr[0]
        
#         for i in range(1,len(arr)):
#             num = arr[i]
            
#             if num < 0:
#                 max_ending_here , min_ending_here = min_ending_here , max_ending_here
            
#             max_ending_here = max(num , num* max_ending_here)
#             min_ending_here = min(num , num * min_ending_here)
            
#             max_so_far = max(max_so_far , max_ending_here)
            
#         return max_so_far

# #Day12
# class Solution:
#     def kadane(self, arr):
#         max_ending = max_so_far = arr[0]
#         for x in arr[1:]:
#             max_ending = max(x , max_ending+x)
#             max_so_far = max(max_so_far , max_ending)
#         return max_so_far
        
    
#     def min_kadane(self , arr):
#         min_ending = min_so_far = arr[0]
#         for x in arr[1:]:
#             min_ending = min(x , min_ending+x)
#             min_so_far = min(min_so_far , min_ending)
#         return min_so_far
        
#     def circularSubarraySum(self , arr):
#         total_sum = sum(arr)
#         max_kadane = self.kadane(arr)
#         min_kadane = self.min_kadane(arr)
        
#         if max_kadane < 0:
#             return max_kadane
        
#         return max(max_kadane , total_sum - min_kadane)

class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        i = 0
        
        while i < n:
            co_idx = arr[i] - 1
            if 1 <= arr[i] <= n and arr[i] != arr[co_idx]:
                arr[i] , arr[co_idx] = arr[co_idx] , arr[i]
            else:
                i+=1
        
        for i in range(n):
            if arr[i] != i+1 :
                return i+1
        
        return n+1
                
