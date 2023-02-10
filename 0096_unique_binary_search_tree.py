'''

Catalan number:
n = 0  -> 1
n = 1  -> 1
n = 2  -> c0 * c1 + c1 * c0 
n = 3  -> c0 * c2 + c1 * c1 + c2 * c0
n = 4  -> c0 * c3 + c1 * c2 + c2 * c1 + c3 * c0

'''

class Solution:
    def numTrees(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0] = 1
        memo[1] = 1
        
        def num_tree_helper(num):
            if (memo[num] != 0):
                return memo[num]
            else:
                for i in range(num):
                    memo[num] += num_tree_helper(i) * num_tree_helper(num - i - 1)
                
                return memo[num]
            
        num_tree_helper(n)
        return memo[n]