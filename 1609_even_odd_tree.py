# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        odd_level = True
        queue = [root]
        while queue:
            odd_level = not odd_level

            tmp_queue = []
            prev_val = None
            for node in queue:
                if odd_level and node.val % 2 != 0:
                    return False
                
                if not odd_level and node.val % 2 == 0:
                    return False
                
                if prev_val != None:
                    if odd_level and prev_val <= node.val:
                        return False
                    
                    if not odd_level and prev_val >= node.val:
                        return False
                
                prev_val = node.val
                if node.left != None:
                    tmp_queue.append(node.left)
                
                if node.right != None:
                    tmp_queue.append(node.right)
            
            queue = tmp_queue
        return True
                    
                    


