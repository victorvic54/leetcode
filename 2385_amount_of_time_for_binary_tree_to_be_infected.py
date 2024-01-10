# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def findDepth(self, root):
        depth = -1
        if root == None:
            return depth

        queue = []
        queue.append(root)
        while queue:
            depth += 1
            tmp_queue = []
            for node in queue:
                if node.left != None:
                    tmp_queue.append(node.left)
                
                if node.right != None:
                    tmp_queue.append(node.right)
            
            queue = tmp_queue
        
        return depth

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def traverse(root):
            if root == None:
                return None, -1

            encountered, maxDepth = traverse(root.left)
            if encountered != None:
                maxDepth = max(maxDepth, 1 + self.findDepth(root.right) + encountered)
                return encountered + 1, maxDepth
                
            if root.val == start:
                return 1, self.findDepth(root)

            encountered, maxDepth = traverse(root.right)
            if encountered:
                maxDepth = max(maxDepth, 1 + self.findDepth(root.left) + encountered)
                return encountered + 1, maxDepth

            return None, maxDepth

        _, maxDepth = traverse(root)
        return maxDepth
