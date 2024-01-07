class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        counter = defaultdict(list)
        for i in range(len(nums)):
            counter[nums[i]].append(i)
            
        memo = {}
        def backtracking(idx, diff, count):
            if (idx, diff, count) in memo:
                return memo[(idx, diff, count)]
            
            ans = 0
            if count >= 3:
                ans += 1
            
            if nums[idx] + diff in counter:
                for next_idx in counter[nums[idx] + diff]:
                    if idx < next_idx:
                        ans += backtracking(next_idx, diff, count + 1)

            memo[(idx, diff, count)] = ans
            return ans

        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):             
                ans += backtracking(j, nums[j] - nums[i], 2)
        return ans

