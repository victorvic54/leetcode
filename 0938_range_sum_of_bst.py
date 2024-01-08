# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def backtracking(root):
            if root == None:
                return 0
            
            if root.val < low:
                return backtracking(root.right)
            elif root.val > high:
                return backtracking(root.left)
            else:
                return root.val + backtracking(root.left) + backtracking(root.right)
        
        return backtracking(root)

