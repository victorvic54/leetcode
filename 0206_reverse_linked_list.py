# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # ITERATIVE
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
            
        while (head):
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            
        return prev
    
    
    # RECURSION
    
    def reverseList(self, head: ListNode) -> ListNode:
        return self.helper(head, None)
    
    def helper(self, head: ListNode, prev: ListNode):
        if (not head):
            return prev
        
        curr = head
        head = head.next
        curr.next = prev
        
        return self.helper(head, curr)