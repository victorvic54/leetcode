# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree_map = defaultdict(list)

        def backtracking(root, depth):
            if root == None:
                return
            
            backtracking(root.left, depth + 1)
            tree_map[depth].append(root.val)
            backtracking(root.right, depth + 1)
            return
        
        backtracking(root, 0)
        result = []
        for i in range(len(tree_map)):
            result.append(tree_map[i])
        return result

# N = number of nodes
# Time: O(N)
# Space: O(N)

