# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = []
        def backtracking(node, max_num):
            if node == None:
                return

            if node.val >= max_num:
                good_nodes.append(node)
            
            max_num = max(max_num, node.val)
            backtracking(node.left, max_num)
            backtracking(node.right, max_num)
            return
        
        backtracking(root, root.val)
        return len(good_nodes)

# N = number of nodes
# Time: O(N)
# Space: O(N)
