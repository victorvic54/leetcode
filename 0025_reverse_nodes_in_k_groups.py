# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# Using this example:  1->2->3->4->5
# when k = 2, expected:  2->1->4->3->5

class Solution:
    #############
    # Iterative #
    #############
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        result = head
        
        # Go to the k-1 index (In example: result points to the number 2)
        for i in range(k - 1):
            result = result.next
            
        while True:
            count = k
            prev = None

            # Leetcode #206 reverse a linked list but using count to limit/stop
            while (head and count > 0):
                curr = head
                head = head.next
                curr.next = prev
                prev = curr
                
                count -= 1
            
            # prev will return 2 -> 1, 4 -> 3, etc
            # head is pointing to node with value 3 -> 4 -> 5, 5 respectively
            tmp_pointer = prev
            head_pointer = head
            
            # we want the node 1 in 2 -> 1 to point to node 4 in 3 -> 4 -> 5
            for i in range(k - 1):
                tmp_pointer = tmp_pointer.next
            
            
            # We run this to check whether there will be enough 
            # k nodes to reverse in next iteration
            for i in range(k - 1):                
                if (not head_pointer):          # To tackle cases where head: 1 -> 2 and k = 2
                    tmp_pointer.next = head
                    return result

                head_pointer = head_pointer.next        
 
            if (not head_pointer):              # To tackle cases where head: 1 -> 2 -> 3 and k = 1
                tmp_pointer.next = head
                return result

            tmp_pointer.next = head_pointer
            
        return result
 

    #############
    # Recursion #
    #############

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        count = 0
        
        while (curr and count != k):  # find the k+1 node
            curr = curr.next
            count += 1
        
        if (count == k):  # if k+1 node is found, it means we can reverse in group of k
            curr = self.reverseKGroup(curr, k)  # reverse list with k+1 node as head
            
            # head - head-pointer to direct part, 
            # curr - head-pointer to reversed part;
            
            while (count > 0):    # reverse current k-group: 
                tmp = head.next   # tmp - next head in direct part
                head.next = curr  # preappending "direct" head to the reversed list 
                curr = head       # move head of reversed part to a new node
                head = tmp        # move "direct" head to the next node in direct part
                count -= 1

            head = curr
    
        return head