# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        num_nodes = 1
        slow = head
        fast = head

        if (head == None or head.next == None):
            return head
        
        # Count number of nodes in the linkedlist
        while (fast.next != None):
            fast = fast.next
            num_nodes += 1
        
        # check how many times we need to rotate
        k = k % num_nodes
        
        if (k == 0):
            return head
        
        # since fast already point to the place before None, we just need to move the slow pointer
        # example:
        # 1 -> 2 -> 3 -> 4 -> 5 -> None   and   k = 2
        #          slow      fast
        for i in range(num_nodes - k - 1):
            slow = slow.next
        
        result = slow.next
        fast.next = head
        slow.next = None
        
        return result
    
    
    # Another solution without counting the num_nodes (but can be not efficient)
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (head == None or head.next == None or k == 0):
            return head
        
        fast = head
        slow = head
        
        for i in range(k):
            if (fast.next == None):
                fast = head
            else:
                fast = fast.next
                
        while (fast.next != None):
            fast = fast.next
            slow = slow.next
            
        fast.next = head
        result = slow.next
        slow.next = None
        
        return result
