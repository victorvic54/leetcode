# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        tmp = ListNode(0)
        tmp.next = head
        result = tmp
        
        for _ in range(1, m):
            tmp = tmp.next
        
        before_m = tmp
        tmp = tmp.next
        
        prev = None
        counter = n - m

        # reverse a linkedlist
        while (tmp and counter >= 0):
            curr = tmp
            tmp = tmp.next
            curr.next = prev
            prev = curr
            counter -= 1

        before_m.next.next = tmp
        before_m.next = curr
        
        return result.next