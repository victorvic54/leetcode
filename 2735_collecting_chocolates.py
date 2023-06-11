class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        res = [x * k for k in range(n)]
        for i in range(n):
            cur = nums[i] # I want to select this particular type i
            for k in range(n): # Try all possible rotation with the associated cost and only get the minimum
                cur = min(cur, nums[i - k])
                res[k] += cur # Add the cost of rotation to add this particular type i after k rotation
        return min(res)
