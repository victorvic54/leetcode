class Solution:
    # monotonic stack from front
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        s = []
        for cur, cur_tmp in enumerate(T):
            while s and cur_tmp > T[s[-1]]:
                ans[s[-1]] = cur - s[-1]
                s.pop()
            s.append(cur)
        return ans
    
    # monotonic stack from back
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        s = []
        for cur in range(len(T) - 1, -1, -1):
            cur_tmp = T[cur]
            while s and cur_tmp >= T[s[-1]]:
                s.pop()
            
            if s and cur_tmp < T[s[-1]]:
                ans[cur] = s[-1] - cur

            s.append(cur)
        return ans

# Time: O(n)
# Space: O(n)
