class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        self.memo = defaultdict(int)
        self.nums = nums
        self.target = target
        
        is_possible, max_jumps = self.backtracking(0)
        if is_possible:
            return max_jumps
        else:
            return -1

    def backtracking(self, prev):        
        if prev in self.memo:
            return self.memo[prev]

        if prev == len(self.nums) - 1:
            return (True, 0)

        max_jumps = 0
        max_possible = False
        for i in range(prev + 1, len(self.nums)):
            if not (-self.target <= self.nums[i] - self.nums[prev] <= self.target):
                continue
            
            is_possible, tmp_jumps = self.backtracking(i)      
            if is_possible:
                max_possible = True
                max_jumps = max(max_jumps, tmp_jumps + 1)
          
        self.memo[prev] = (max_possible, max_jumps)
        return (max_possible, max_jumps)
