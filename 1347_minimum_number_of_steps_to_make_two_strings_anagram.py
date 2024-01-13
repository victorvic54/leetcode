class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff_dict = defaultdict(int)
        for i in range(len(s)):
            diff_dict[s[i]] += 1
            diff_dict[t[i]] -= 1
        
        ans = 0
        for key in diff_dict:
            ans += abs(diff_dict[key])
        
        return ans // 2

