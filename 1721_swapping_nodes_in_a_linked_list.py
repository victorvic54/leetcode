# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# One Pass Solution
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front = head
        back = head
        tail = head

        for _ in range(k - 1):
            tail = tail.next
        
        while k - 1 > 0 or tail.next != None:
            if k - 1 > 0:
                front = front.next
                k -= 1
            
            if tail.next != None:
                back = back.next
                tail = tail.next
        
        tmp = front.val
        front.val = back.val
        back.val = tmp

        return head
