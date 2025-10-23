# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        tree_map = defaultdict(list)
        def backtracking(node, depth):
            if node == None:
                return

            backtracking(node.left, depth + 1)
            tree_map[depth].append(node.val)
            backtracking(node.right, depth + 1)
            return
        
        backtracking(root, 0)
        result = []
        for i in range(len(tree_map)):
            result.append(tree_map[i][-1])
        return result

# N = number of nodes
# Time: O(N)
# Space: O(N)
