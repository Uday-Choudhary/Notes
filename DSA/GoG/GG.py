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

# from typing import List


# class Solution:
#     # Function to rotate an array by d elements in counter-clockwise direction.
#     def rotateArr(self, arr, d):
#         n = len(arr)
#         d = d % n
#         pos = 0
#         stored_part = []
#         for i in range(d):
#             stored_part.append(arr[i])

#         for i in range(d, n):
#             arr[pos] = arr[i]
#             pos += 1

#         for i in range(d):
#             arr[pos] = stored_part[i]
#             pos += 1

#         return arr


# # Day 7
# class Solution:
#     def maximumProfit(self, prices) -> int:
#         profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1]:
#                 profit += prices[i] - prices[i-1]
#         return profit

#Day 8
#User function Template for python3

# class Solution:
#     def getMinDiff(self, arr,k):
#         n = len(arr)
#         arr.sort()
#         initial_diff = arr[-1] - arr[0]
#         smallest = arr[0] + k
#         largest = arr[-1] - k
#         min_diff = initial_diff
        
#         for i in range(n-1):
#             min_elem = min(smallest , arr[i+1] - k)
#             max_elem = max(largest, arr[i] + k)
            
#             if min_elem < 0:
#                 continue
#             min_diff = min(min_diff , max_elem - min_elem)
#         return min_diff
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
#Day13
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
#Day14 Strings
#User function template for Python
# class Solution:
#     def myAtoi(self, s):
#         i,n,sign,num = 0 , len(s), 1,0
#         INT_MAX , INT_MIN = 2**31 -1 , -2 **31
        
#         while i < n and s[i] == ' ' :
#             i+=1
#         if i < n and s[i] in '+-':
#             sign = -1 if s[i] == '-' else 1
#             i+=1
            
#         while i<n and '0' <= s[i] <= '9':
#             digit = ord(s[i]) - ord('0')
#             if num > (INT_MAX - digit) // 10:
#                 return INT_MAX if sign == 1 else INT_MIN
#             num = num * 10 + digit
#             i+=1
#         return sign * num

#Day15 
#User function Template for python3
# class Solution:
# 	def addBinary(self, s1, s2):
# 		# code here
# 		i,j = len(s1) - 1 , len(s2) - 1
# 		carry = 0
# 		result = []
		
# 		while i>= 0 or j >=0 or carry:
# 		    bit1 = int(s1[i]) if i>= 0 else 0
# 		    bit2 = int(s2[j]) if j >= 0 else 0
# 		    total = bit1 + bit2 + carry
		    
# 		    result.append(str(total % 2))
# 		    carry = total // 2
		    
# 		    i-=1
# 		    j-=1
		    
		    
# 	    result_str = ''.join(reversed(result)).lstrip('0')
	    
# 	    return result_str if result_str else '0'
# Day16
# class Solution:
#     def areAnagrams(self, s1, s2):
#        # code here
#         if len(s1) != len(s2):
#             return False
           
#         freq1 = [0] * 26
#         freq2 = [0] * 26
        
#         for char in s1:
#             freq1[ord(char) - ord('a')] += 1
            
#         for char in s2:
#             freq2[ord(char) - ord('a')] += 1


# #Day17
# class Solution:
#     def nonRepeatingChar(self,s):
#         #code here
    
#         freq = {}
        
#         for ch in s:
#             freq[ch] = freq.get(ch , 0) + 1
            
#         for ch in s:
#             if freq[ch] == 1:
#                 return ch
        
#         return '$'
            
#         return freq1 == freq2

#Day18
#User function Template for python3

# class Solution:
#     def search(self, pat, txt):
#         # code here
#         def computeLPS(pattern):
#             lps = [0] * len(pattern)
#             length = 0
#             i = 1
            
#             while i < len(pattern):
#                 if pattern[i] == pattern[length]:
#                     length +=1
#                     lps[i] = length
#                     i+=1
                
#                 else:
#                     if length != 0:
#                         length = lps[length - 1]
#                     else:
#                         lps[i] = 0
#                         i+=1
#             return lps
            
#         m,n = len(pat) , len(txt)
#         lps = computeLPS(pat)
#         result = []
        
#         i=j=0
#         while i < n:
#             if pat[j] == txt[i]:
#                 i+=1
#                 j+=1
#             if j == m:
#                 result.append(i-j)
#                 j = lps[j-1]
                
#             elif i< n and pat[j] != txt[i]:
#                 if j!= 0:
#                     j = lps[j-1]
#                 else:
#                     i+=1
#         return result
#Day19
# class Solution:
#     def minChar(self, s):
#         #Write your code here
#         rev_s = s[::-1]
#         temp = s + '#' + rev_s
#         lps = [0] * len(temp)
        
#         for i in range(1 , len(temp)):
#             l = lps[i-1]
#             while l > 0 and temp[i] != temp[l]:
#                 l = lps[l-1]
#             if temp[i] == temp[l]:
#                 l+=1
            
#             lps[i] = l
            
#         return len(s) - lps[-1]

# #Day20
# #User function Template for python3

# class Solution:
    
#     #Function to check if two strings are rotations of each other or not.
#     def areRotations(self,s1,s2):
#         #code here
#         if len(s1) != len(s2):
#             return False
#         return s2 in (s1 + s1)

# #Day21
# class Solution:
#     # Function to sort an array of 0s, 1s, and 2s
#     def sort012(self, arr):
#         # code here
#         n = len(arr)
#         low,mid,high = 0,0,n-1
        
#         while(mid <= high):
#             if arr[mid] == 0:
#                 arr[low] , arr[mid] = arr[mid] , arr[low]
#                 low+=1
#                 mid+=1
#             elif arr[mid] == 1:
#                 mid+=1
#             else:
#                 arr[mid] , arr[high] = arr[high] , arr[mid]
#                 high-=1
        
#         return arr

# #Day22
# #User function Template for python3
# class Solution:
#     # Function to find hIndex
#     def hIndex(self, citations):
#         #code here
#         n = len(citations)
#         count = [0] *(n+1)
        
#         for c in citations:
#             if c >= n:
#                 count[n] +=1
#             else:
#                 count[c] +=1
                
#         total = 0
#         for h in range(n,-1,-1):
#             total+=count[h]
#             if total >= h:
#                 return h
#         return 0

#day23
class Solution:
    def inversionCount(self, arr):
        # Code Here
        n = len(arr)
        return self.mergeSort(arr,0,n-1)
        
    def mergeSort(self , arr, left , right):
        inv_count = 0
        if left < right:
            mid = (left+ right) // 2
            inv_count += self.mergeSort(arr,left,mid)
            inv_count += self.mergeSort(arr,mid+1, right)
            inv_count += self.merge(arr,left,mid,right)
            
        return inv_count
        
    
    def merge(self,arr,left,mid,right):
        temp = []
        i = left
        j = mid+1
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j] :
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                inv_count += (mid - i + 1)
                j+=1
                
        while i <= mid:
            temp.append(arr[i])
            i+=1
        while j <= right:
            temp.append(arr[j])
            j+=1
            
        for i in range(len(temp)):
            arr[left+i] = temp[i]
            
        return inv_count
