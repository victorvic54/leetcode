class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}
        def backtracking(index):
            if index in memo:
                return memo[index]

            if index >= len(arr):
                return 0

            max_sum = 0
            max_num = 0
            for i in range(index, index + k):
                if i >= len(arr):
                    break

                max_num = max(max_num, arr[i])
                max_sum = max(max_sum, (max_num * (i-index+1)) + backtracking(i + 1))
            
            memo[index] = max_sum
            return max_sum
        
        return backtracking(0)

