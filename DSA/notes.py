print("Hello Hello ")

#Insert node at the given position

'''
    {
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
def addElement(head, M, K):
    fast = head
    slow = head
    new_node = Node(K)

    if M == 1:
        new_node.next = head
        return new_node

    if head is None:
        return None
    


    for _ in range(M-2):
        fast = fast.next
    preserve_fast_next = fast.next
    fast.next = new_node
    new_node.next = preserve_fast_next

    return head

#Delete the Kth node from the end

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
'''
def deleteElement(head, k):
    fast = head
    slow = head

    for _ in range(k):
        fast = fast.next

    #k = len list ho gaya to piche se k mtlb 1st element so head.next kar daynge return head delete ho jayga
    
    if not fast:
        return head.next  # new head

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return head