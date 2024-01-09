# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSequence(self, root):
        if root == None:
            return []

        if root.left == None and root.right == None:
            return [root.val]
        
        result = self.leafSequence(root.left) + self.leafSequence(root.right)
        return result

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leafSequence(root1) == self.leafSequence(root2)
