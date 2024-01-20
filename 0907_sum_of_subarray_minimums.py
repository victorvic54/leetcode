"""
Stack data structure: Previous Less Element (PLE)
prev_less for [3,1,2,5,4] is [-1,-1,1,2,2]
next_less for [3,1,2,5,4] is [1,-1,-1,4,-1]

prev_less for [2,4,5,3,1] is [-1,0,1,0,-1]
next_less for [2,4,5,3,1] is [4,3,3,4,-1]

prev_less = [-1] * len(arr)
stack = []
for i in range(len(arr)):
    while stack and arr[stack[-1]] > arr[i]:
        stack.pop()
    if len(stack) != 0:
        prev_less[i] = stack[-1]
    stack.append(i)

next_less = [-1] * len(arr)
stack = []
for i in range(len(arr)):
    while stack and arr[stack[-1]] > arr[i]:
        x = stack.pop()
        next_less[x] = i
    stack.append(i)

How I derive the pattern:
# [4]                           -> 4
# [2],[2,4]                     -> 2, 2
# [1],[1,2],[1,2,4]             -> 1, 1, 1
# [3],[3,1],[3,1,2],[3,1,2,4]   -> 3, 1, 1, 1
-> dp = [6,3,4,4]

# [3]
# [43],[43,3]
# [94],[94,43],[94,43,3]
# [81],[81,94],[81,94,43],[81,94,43,3]
# [11],[11,81],[11,81,94],[11,81,94,43],[11,81,94,43,3]
-> dp = [47,208,140,46,3]
"""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Stack data structure: Next Less Element (NLE)
        # next_less for [3,1,2,5,4] is [1,-1,-1,4,-1]
        # next_less for [2,4,5,3,1] is [4,3,3,4,-1]
        next_less = [-1] * len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                x = stack.pop()
                next_less[x] = i
            stack.append(i)

        MOD = 10**9 + 7
        dp = [None] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr) - 1:
                dp[i] = arr[i]
                continue
            
            dp[i] = 0
            if arr[i] >= arr[i+1]:
                dp[i] = arr[i] + dp[i+1]
            else:
                if next_less[i] == -1:
                    dp[i] = (len(arr) - i) * arr[i]
                else:
                    dp[i] = (next_less[i] - i) * arr[i] + dp[next_less[i]]

        return sum(dp) % MOD

