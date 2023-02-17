# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderTraversal(self, root):
        if root.val != None:
            self.nodes.append(root.val)

        if root.left:
            self.inOrderTraversal(root.left)

        if root.right:
            self.inOrderTraversal(root.right)
        
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.nodes = []
        self.inOrderTraversal(root)
        self.nodes.sort()

        minDiff = float('inf')
        prev = None
        for node in self.nodes:
            if prev == None:
                prev = node
                continue
            
            minDiff = min(minDiff, abs(node - prev))
            prev = node
        
        return minDiff
