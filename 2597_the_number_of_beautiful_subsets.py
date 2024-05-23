class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtracking(idx, k, mp) -> int:
            if idx == len(nums):
                return 1

            total = 0
            if mp[nums[idx] - k] == 0 and mp[nums[idx] + k] == 0:
                mp[nums[idx]] += 1
                total += backtracking(idx + 1, k, mp)
                mp[nums[idx]] -= 1
            
            total += backtracking(idx + 1, k, mp)
            
            return total

        mp = defaultdict(int)
        ans = backtracking(0, k, mp)
        return ans - 1

