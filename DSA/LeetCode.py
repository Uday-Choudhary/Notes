# # Maximum points you can obtain from cards #1423

# def maxScore(nums, k):
#     left_sum = 0
#     right_sum = 0
#     max_sum = 0

#     for i in range(k):
#         left_sum += nums[i]
#     max_sum = left_sum

#     right_index = len(nums) - 1
#     for i in range(k-1, -1, -1):
#         left_sum -= nums[i]
#         right_sum += nums[right_index]
#         right_index -= 1
#         max_sum = max(max_sum, left_sum+right_sum)
#         # print(max_sum)

#     return max_sum


# nums = list(map(int, input().split()))
# k = int(input())

# print(maxScore(nums, k))
# # phele 4 term ka sum liya left me dala fir kam karte gye or right add karte gye of sabka max jo banta jaa rha tha usko max me update karte gye


# # Search in Rotated Sorted Arr
# nums = list(map(int, input().split()))
# target = int(input())
# point = 0

# for i in range(1, len(nums)):
#     if nums[i] < nums[i-1]:
#         point = i
#         break

# if nums[point - 1] >


# def rotatedSearch1(nums, target):
#     low = point
#     high = len(nums) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#         return -1


# def rotatedSearch2(nums, target):
#     low = 0
#     high = point - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#         return -1


# ans1 = rotatedSearch1(nums, target)
# ans2 = rotatedSearch2(nums, target)

# if ans1 == -1 and ans2 == -1:
#     print(-1)
# else:
#     print(ans1 if ans1 != -1 else ans2)


# Search in Rotated Sorted Arr II
# def searchInARotatedSortedArrayII(arr: List[int], k: int) -> bool:
#     n = len(arr)  # size of the array
#     low, high = 0, n - 1

#     while low <= high:
#         mid = (low + high) // 2

#         # if mid points to the target
#         if arr[mid] == k:
#             return True

#         # Edge case:
#         if arr[low] == arr[mid] and arr[mid] == arr[high]:
#             low += 1
#             high -= 1
#             continue

#         # if left part is sorted
#         if arr[low] <= arr[mid]:
#             if arr[low] <= k <= arr[mid]:
#                 # element exists
#                 high = mid - 1
#             else:
#                 # element does not exist
#                 low = mid + 1
#         else:  # if right part is sorted
#             if arr[mid] <= k <= arr[high]:
#                 # element exists
#                 low = mid + 1
#             else:
#                 # element does not exist
#                 high = mid - 1

#     return False


# 540. Single Element in a Sorted Array

# Approch - starting me even-odd pe same value hogi and single value ke bad odd-even pe same value hogi usi hisab se rejection kara h binery search me
# class Solution:
#     def singleNonDuplicate(self, arr: List[int]) -> int:
#         low = 0
#         n = len(arr)
#         high = n - 1

#         if len(arr) == 1:
#             return arr[0]

#         if arr[0] != arr[1]:
#             return arr[0]

#         if arr[n - 1] != arr[n - 2]:
#             return arr[n - 1]

#         while high >= low:
#             mid = (low + high) // 2

#             if mid % 2 == 0:
#                 if arr[mid] == arr[mid + 1]:
#                     low = mid + 1
#                 elif arr[mid] == arr[mid - 1]:
#                     high = mid - 1
#                 else:
#                     return arr[mid]

#             else:
#                 if arr[mid] == arr[mid - 1]:
#                     low = mid + 1
#                 elif arr[mid] == arr[mid + 1]:
#                     high = mid - 1
#                 else:
#                     return arr[mid]

# Minimum Number of Days to Make m Bouquets
# def minDays(bloomDay, m, k):
#     ans = -1

#     if len(bloomDay) < k * m:
#         return ans

#     def canMake(mid):
#         bouquets = 0
#         flowers = 0
#         for days in bloomDay:
#             if days <= mid:
#                 flowers += 1
#                 if flowers == k:
#                     bouquets += 1
#                     flowers = 0
#             else:
#                 flowers = 0
#         return bouquets >= m

#     low = min(bloomDay)
#     high = max(bloomDay)

#     while low <= high:
#         mid = (low + high) // 2
#         if canMake(mid):
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1

#     return ans


# # Input
# bloomDay = list(map(int, input().split()))
# m, k = map(int, input().split())

# print(minDays(bloomDay, m, k))

# ''' check function mid le rha h dekh rha h days mid se  kam ya equal h to ek flower khil 
# jayga aise contine jitni bar ho rh h flower bada rhe h if flower = k ho rhe h to bouket +
# 1 kar rhe h or flower ko vapas 0 kar rhe h kyoki ek bouke ban gaya h nai karnge to flower 
# badtee jaynge vapas k vali condition check he nai hogi orrr day jab bhi jyada aa jye mtlb or time 
# lagega uss day flower bloom nai hoga to abhi tak ki strek flower = 0 kar daynge'''
