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
