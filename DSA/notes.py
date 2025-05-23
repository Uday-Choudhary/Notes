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
# 2d to 1d matrix
# rows = len(matrix)
# cols = len(matrix[0])

# for index in range(rows * cols):
#     row = index // cols
#     col = index % cols
#     print(matrix[row][col], end=' ')

def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):  # Start from the second element (index 1)
        key = seq[i]
        j = i - 1
        while j >= 0 and seq[j] > key:  # Shift elements to the right
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = key  # Insert key at the correct position
    return seq  # Return the sorted list

# import React, { useState } from 'react';

# const ItemList = () => {
#   const items = [
#     { name: 'Apple', details: 'A sweet red fruit, high in vitamins.' },
#     { name: 'Banana', details: 'A yellow fruit, rich in potassium.' },
#     { name: 'Orange', details: 'A citrus fruit, packed with vitamin C.' },
#   ];

#   const [showDetails, setShowDetails] = useState(false);

#   return (
#     <div>
#       <button onClick={() => setShowDetails(!showDetails)}>
#         {showDetails ? 'Hide All Details' : 'Show All Details'}
#       </button>
#       {showDetails && items.map((item, index) => (
#         <div key={index}>
#           <strong>{item.name}</strong>
#           <p>{item.details}</p>
#         </div>
#       ))}
#     </div>
#   );
# };

# export default ItemList;

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''
# def calculateDifference(root):
#     if not root:
#         return 0

#     min_node = root
#     while min_node.left:
#         min_node = min_node.left
#     minimum = min_node.data

#     max_node = root
#     while max_node.right:
#         max_node = max_node.right
#     maximum = max_node.data

#     product = minimum * maximum
#     summation = minimum + maximum

#     return product - summation


# def answerQueries(nums, queries):
#     # Step 1: Sort nums to pick the smallest elements first
#     nums.sort()
    
#     # Step 2: Compute prefix sum array
#     prefix_sum = [0] * len(nums)
#     prefix_sum[0] = nums[0]
#     for i in range(1, len(nums)):
#         prefix_sum[i] = prefix_sum[i - 1] + nums[i]

#     # Step 3: Answer each query using a manual binary search
#     def binary_search(arr, target):
#         left, right = 0, len(arr) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if arr[mid] <= target:
#                 left = mid + 1
#             else:
#                 right = mid - 1


# Dutch Flag Algo
# def sortColors(nums):
#     low, mid = 0, 0
#     high = len(nums) - 1

#     while mid <= high:
#         if nums[mid] == 0:
#             nums[low], nums[mid] = nums[mid], nums[low]
#             low += 1
#             mid += 1
#         elif nums[mid] == 1:
#             mid += 1
#         else:
#             nums[mid], nums[high] = nums[high], nums[mid]
#             high -= 1
#     return nums

#         return left  # The position where the sum is still <= target

#     result = []
#     for q in queries:
#         result.append(binary_search(prefix_sum, q))
    
#     return result

L , R = map(int , input().split())
max_value = 10**6
is_prime = [True] * (max_value+1)

is_prime[0] = False
is_prime[1] = False

for i in range(2 , int(max_value ** 0.5)+1):
    if is_prime[i]:
        for j in range(i*i , max_value+1 , i):
            is_prime[j] = False
 
prime_count = [0] * (max_value+1)

for i in range(1 , max_value+1):
    prime_count[i] = prime_count[i-1] + (1 if is_prime[i] else 0)

if L == 0:
    print(prime_count[R])


I have sooo much work to do man

else:
    print(prime_count[R] - prime_count[L-1])
