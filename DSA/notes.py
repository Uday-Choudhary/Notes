# print("Hello Hello ")

# #Insert node at the given position

# '''
#     {
#         class Node:
#             def __init__(self, data):   # data -> value stored in node
#                 self.data = data
#                 self.next = None
#     }
# '''
# def addElement(head, M, K):
#     fast = head
#     slow = head
#     new_node = Node(K)

#     if M == 1:
#         new_node.next = head
#         return new_node

#     if head is None:
#         return None
    


#     for _ in range(M-2):
#         fast = fast.next
#     preserve_fast_next = fast.next
#     fast.next = new_node
#     new_node.next = preserve_fast_next

#     return head

# #Delete the Kth node from the end

# '''
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
# '''
# def deleteElement(head, k):
#     fast = head
#     slow = head

#     for _ in range(k):
#         fast = fast.next

#     #k = len list ho gaya to piche se k mtlb 1st element so head.next kar daynge return head delete ho jayga
    
#     if not fast:
#         return head.next  # new head

#     while fast.next:
#         fast = fast.next
#         slow = slow.next

#     slow.next = slow.next.next

#     return head

# # Path Sum
# '''
# class Node:
#     def __init__(self, val=0, left=None, right=None):
#         self.key = val
#         self.left = left
#         self.right = right
# '''
# def has_path_sum(root, target , total = 0) :
    
#     if root is None:
#         return False

#     total+= root.key
    
#     if (total == target) and (root.left == None and root.right == None):
#         return True

#     left_ans = has_path_sum(root.left , target , total)
#     right_ans = has_path_sum(root.right , target , total)
    
#     return left_ans or right_ans

# # Level Order Traversal of Binary Tree
# from collections import deque
# '''
# class Node:
#     def __init__(self, val=0):
#         self.val = val
#         self.left = None
#         self.right = None
# '''

# def level_order_traversal(root):
#     if not root:
#         return []
    
#     result = []
#     queue = deque([root])
    
#     while queue:
#         level_size = len(queue)
#         level_nodes = []
        
#         for _ in range(level_size):
#             node = queue.popleft()
#             level_nodes.append(node.val)
            
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
        
#         result.append(level_nodes)
    
#     return result
#Day8
class Solution:
    def maximumProfit(self, prices):
        # code here
        min_price = float('inf')
        max_profit = 0
        
        for i in prices:
            if i < min_price:
                min_price = i
            else:
                profit = i - min_price
                max_profit = max(max_profit , profit)
        return max_profit

# Two Sum
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []


# Reverse Linked List
# Given the head of a singly linked list, reverse the list and return the reversed list.
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


# Valid Parentheses
# Given a string s containing just the characters ( ) { } [ ],
# determine if the input string is valid.
class Solution:
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else "#"
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack


# Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a sorted list.
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummy.next


# Maximum Subarray - Kadane's Algorithm
# Find the contiguous subarray which has the largest sum and return its sum.
class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum


# Binary Search
# Given a sorted array of integers and a target, return the index if found, else -1.
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can climb 1 or 2 steps. How many distinct ways can you climb?
class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


# Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself.
class Solution:
    def isSymmetric(self, root):
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        if not root:
            return True
        return isMirror(root.left, root.right)


# Single Number
# Given a non-empty array where every element appears twice except one, find that single one.
# XOR approach - O(n) time, O(1) space
class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result


# Intersection of Two Linked Lists
# Find the node at which two singly linked lists intersect.
class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        pointerA = headA
        pointerB = headB
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        return pointerA


# Majority Element
# Given an array nums, find the element that appears more than n/2 times.
# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


# Move Zeroes
# Move all 0s to the end of array while maintaining relative order of non-zero elements.
class Solution:
    def moveZeroes(self, nums):
        write_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write_pos], nums[i] = nums[i], nums[write_pos]
                write_pos += 1
        return nums


# Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome.
class Solution:
    def isPalindrome(self, head):
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next
        return vals == vals[::-1]


# Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter (longest path between any two nodes).
class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        depth(root)
        return self.diameter


# Invert Binary Tree
# Given the root of a binary tree, invert the tree and return its root.
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# Subarray Sum Equals K
# Given an array of integers and an integer k,
# find the total number of subarrays whose sum equals k.
class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        return count


# Find All Duplicates in an Array
# Given an array where 1 <= a[i] <= n, find all elements that appear twice.
class Solution:
    def findDuplicates(self, nums):
        result = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] = -nums[index]
        return result


# Rotate Array
# Given an array, rotate it to the right by k steps.
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        return nums


# Product of Array Except Self
# Given an integer array nums, return an array where answer[i] is the product
# of all elements except nums[i], without using division.
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        return result


# Sort Colors - Dutch National Flag Problem
# Given an array with n objects colored red (0), white (1), or blue (2),
# sort them in-place so that same colors are adjacent.
class Solution:
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums


# Container With Most Water
# Given n non-negative integers representing vertical lines,
# find two lines that together with x-axis form a container with the most water.
class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_water = max(max_water, width * h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


# Trapping Rain Water
# Given n non-negative integers representing an elevation map,
# compute how much water it can trap after raining.
class Solution:
    def trap(self, height):
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water



# Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals.
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


# Insert Interval
# Insert a new interval into a sorted array of non-overlapping intervals and merge if necessary.
class Solution:
    def insert(self, intervals, newInterval):
        result = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                return result + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        result.append(newInterval)
        return result


# Non-overlapping Intervals
# Find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals: return 0
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        return count


# Meeting Rooms
# Determine if a person could attend all meetings.
class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True


# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements.
class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return sorted(count.keys(), key=lambda x: count[x], reverse=True)[:k]


# Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest = max(longest, current_streak)
        return longest


# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            count[char] = count.get(char, 0) - 1
            if count[char] < 0:
                return False
        return True


# Group Anagrams
# Given an array of strings strs, group the anagrams together.
class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            anagrams[sorted_s].append(s)
        return list(anagrams.values())
\n\n# Find Minimum in Rotated Sorted Array\nclass Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: left = mid + 1
            else: right = mid
        return nums[left]
\n\n# Search in Rotated Sorted Array\nclass Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: right = mid - 1
                else: left = mid + 1
            else:
                if nums[mid] < target <= nums[right]: left = mid + 1
                else: right = mid - 1
        return -1
\n\n# Maximum Product Subarray\nclass Solution:
    def maxProduct(self, nums):
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
\n\n# Coin Change\nclass Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
\n\n# Longest Increasing Subsequence\nclass Solution:
    def lengthOfLIS(self, nums):
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]: LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
\n\n# Word Break\nclass Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
             for w in wordDict:
                 if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                     dp[i] = dp[i + len(w)]
                 if dp[i]: break
        return dp[0]
\n\n# Combination Sum\nclass Solution:
    def combinationSum(self, candidates, target):
        res = []
        def dfs(i, cur, total):
            if total == target: res.append(cur.copy()); return
            if i >= len(candidates) or total > target: return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res
\n\n# House Robber\nclass Solution:
    def rob(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
             temp = max(n + rob1, rob2)
             rob1 = rob2
             rob2 = temp
        return rob2
\n\n# House Robber II\nclass Solution:
    def rob(self, nums):
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
             newRob = max(rob1 + n, rob2)
             rob1 = rob2
             rob2 = newRob
        return rob2
\n\n# Decode Ways\nclass Solution:
    def numDecodings(self, s):
        dp = { len(s): 1 }
        for i in range(len(s) - 1, -1, -1):
             if s[i] == '0': dp[i] = 0
             else: dp[i] = dp[i + 1]
             if (i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456')): dp[i] += dp[i + 2]
        return dp[0]
\n\n# Unique Paths\nclass Solution:
    def uniquePaths(self, m, n):
        row = [1] * n
        for i in range(m - 1):
             newRow = [1] * n
             for j in range(n - 2, -1, -1):
                  newRow[j] = newRow[j + 1] + row[j]
             row = newRow
        return row[0]
\n\n# Jump Game\nclass Solution:
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
             if i + nums[i] >= goal: goal = i
        return goal == 0
\n\n# Clone Graph\nclass Solution:
    def cloneGraph(self, node):
        oldToNew = {}
        def dfs(node):
             if node in oldToNew: return oldToNew[node]
             copy = Node(node.val)
             oldToNew[node] = copy
             for nei in node.neighbors:
                  copy.neighbors.append(dfs(nei))
             return copy
        return dfs(node) if node else None
\n\n# Course Schedule\nclass Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = { i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
             preMap[crs].append(pre)
        visitSet = set()
        def dfs(crs):
             if crs in visitSet: return False
             if preMap[crs] == []: return True
             visitSet.add(crs)
             for pre in preMap[crs]:
                  if not dfs(pre): return False
             visitSet.remove(crs)
             preMap[crs] = []
             return True
        for crs in range(numCourses):
             if not dfs(crs): return False
        return True
