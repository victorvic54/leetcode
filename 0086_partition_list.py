# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(0)
        big = ListNode(0)
        
        result = small
        temp = big
        
        while (head):
            if (head.val < x):
                small.next = ListNode(head.val)
                small = small.next
            else:
                big.next = ListNode(head.val)
                big = big.next
                
            head = head.next
                
        small.next = temp.next
        return result.next