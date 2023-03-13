# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traversal(t1, t2):
            if (not t1 and not t2):
                return True
            
            if (t1 and t2):
                if (t1.val != t2.val):
                    return False
                
                return traversal(t1.left, t2.right) and traversal(t1.right, t2.left)
            else:
                return False
            
        return traversal(root.left, root.right)

