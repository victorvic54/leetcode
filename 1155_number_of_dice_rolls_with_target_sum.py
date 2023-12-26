class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        memo = {}        
        def backtracking(num_dices, num_faces, remainder):
            if (num_dices, num_faces, remainder) in memo:
                return memo[(num_dices, num_faces, remainder)]

            if remainder == 0 and num_dices == 0:
                return 1

            if remainder <= 0 or num_dices == 0:
                return 0
            
            tmp = 0
            for i in range(1, num_faces + 1):
                tmp += backtracking(num_dices - 1, num_faces, remainder - i)
            
            memo[(num_dices, num_faces, remainder)] = tmp
            return tmp % MOD
        
        return backtracking(n, k, target) % MOD
