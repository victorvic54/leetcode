class Solution:
    # Time complexity = O(n^3)
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        counter = defaultdict(list)
        for i in range(len(nums)):
            counter[nums[i]].append(i)

        memo = {}
        def backtracking(idx, diff):
            if (idx, diff) in memo:
                return memo[(idx, diff)]

            ans = 0
            if nums[idx] + diff in counter:
                for next_idx in counter[nums[idx] + diff]:
                    if idx < next_idx:
                        ans += 1 + backtracking(next_idx, diff)

            memo[(idx, diff)] = ans
            return ans

        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ans += backtracking(j, nums[j] - nums[i])
        return ans


    # This solution is TLE
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        memo = [{} for i in range(len(nums))]
        def backtracking(prev, jump):
            if prev != None and jump in memo[prev]:
                return memo[prev][jump]

            ans = 0
            if prev == None:
                counter = 0
            else:
                counter = prev + 1

            for i in range(counter, len(nums)):
                if jump != None:
                    if nums[i] - nums[prev] != jump:
                        continue
                    else:
                        ans += 1

                next_jump = None
                if jump == None:
                    if prev != None:
                        next_jump = nums[i] - nums[prev]
                else:
                    next_jump = jump

                ans += backtracking(i, next_jump)

            if prev != None:
                memo[prev][jump] = ans
            return ans

        return backtracking(None, None)

