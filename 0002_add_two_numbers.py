# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Example:
# (8 -> 7 -> 6) + (6 -> 5 -> 4)
# (4 -> 3 -> 1 -> 1)

# Need to take care of carry and then next of the ListNode is another ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = None
        carry = 0
        
        while True:
            if (l1 and l2):
                total = l1.val + l2.val + carry
                remainder = total % 10
                
                if (res):
                    res.next = ListNode(remainder)
                    res = res.next
                else:
                    res = ListNode(remainder)
                    pointer = res
                
                carry = total // 10
                
                l1 = l1.next
                l2 = l2.next
            elif (l1):
                total = l1.val + carry
                remainder = total % 10
                
                res.next = ListNode(remainder)
                res = res.next
                l1 = l1.next
                
                carry = total // 10
            elif (l2):
                total = l2.val + carry
                remainder = total % 10
                
                res.next = ListNode(remainder)
                res = res.next
                
                l2 = l2.next
                carry = total // 10
            else:
                break
            
            

        if (carry != 0):
            res.next = ListNode(carry)
        
        return pointer
                