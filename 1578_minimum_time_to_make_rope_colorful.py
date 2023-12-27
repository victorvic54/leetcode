class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        memo = {}

        def backtracking(idx, prev):
            tmp_time = float('inf')
            if (idx, prev) in memo:
                return memo[(idx, prev)]

            if idx == len(colors) - 1:
                if prev == colors[idx]:
                    return neededTime[idx]
                return 0
                
            if colors[idx] == prev:
                tmp_time = min(tmp_time, backtracking(idx+1, prev) + neededTime[idx])
            else:
                tmp_time = min(tmp_time, backtracking(idx+1, colors[idx]))
                if colors[idx] == colors[idx+1]:
                    tmp_time = min(tmp_time, backtracking(idx+1, prev) + neededTime[idx])

            memo[(idx, prev)] = tmp_time
            return tmp_time

        return backtracking(0, None)


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        prev = 0 # index of previously retained letter 
        for i in range(1, len(s)): 
            if s[prev] != s[i]:
                prev = i
            else: # use example "aaa" and [3,4,2]
                ans += min(cost[prev], cost[i])
                if cost[prev] < cost[i]:
                    prev = i
        return ans

