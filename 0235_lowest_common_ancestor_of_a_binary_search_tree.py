# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tree_map = {}

        def backtracking(node, path, targets):
            if not node:
                return

            # Add current direction to path
            if node.val in targets:
                tree_map[node.val] = list(path)  # make a copy here only once when found
                targets.remove(node.val)
                if len(targets) == 0:
                    return

            # Try going left
            path.append("left")
            backtracking(node.left, path, targets)
            path.pop()
            path.append("right")
            backtracking(node.right, path, targets)
            path.pop()


        # Build paths to p and q
        backtracking(root, [], {p.val, q.val})
        
        # Find common prefix length
        p_path, q_path = tree_map[p.val], tree_map[q.val]
        min_depth = min(len(p_path), len(q_path))
        ancestor_depth = 0
        while ancestor_depth < min_depth and p_path[ancestor_depth] == q_path[ancestor_depth]:
            i += 1

        # Traverse down from root to the ancestor node
        node = root
        for direction in p_path[:ancestor_depth]:
            node = node.left if direction == "left" else node.right

        return node

# Time: O(N)
# Space: O(H) total
# - Recursion stack up to height H → O(H)
# - Stored paths for p and q 
