# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Lets n denote the number of nodes.
#
# Time Complexity: O(n^2)
# The string representation (triplet) of each subtree can have a length up to O(n)
# Creating each representation therefore costs up to O(n), and we find string representations for all O(n) subtrees during the traversal.
#
# Space Complexity: O(n^2)
# We store all string representations in the hash map. There are O(n) subtrees, and each subtree representation has the length of O(n).

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node):
            if not node:
                return ""

            triplet = ("(" + traverse(node.left) + ")" + str(node.val)
                              + "(" + traverse(node.right) + ")")
            count[triplet] += 1
            if count[triplet] == 2: 
                res.append(node)
            return triplet

        count = collections.defaultdict(int)
        res = []
        traverse(root)
        return res

# To make the solution faster:
# The string representation (triplet) of each subtree should be limited to 3 only -> O(1).
# Better don't use string to represent because string concatenation took slightly some time
# 
# Hence Time and Space Complexity will be O(n)
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node):
            if not node:
                return 0

            triplet = (traverse(node.left), node.val, traverse(node.right))
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1

            id = triplet_to_id[triplet]
            count[id] += 1
            if count[id] == 2:
                res.append(node)
            return id   # return integer not a tuple
        
        triplet_to_id = dict()
        count = collections.defaultdict(int)
        res = []
        traverse(root)
        return res
