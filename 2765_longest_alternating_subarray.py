class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        prev = [1] + [None] * (len(nums) - 1)
        expect_pos = True
        max_len = 0
        
        for i in range(1, len(nums)):
            if expect_pos:            
                expect_num = 1
            else:
                expect_num = -1

            if nums[i] - nums[i-1] == expect_num:
                prev[i] = prev[i - 1] + 1
                expect_pos = not expect_pos
            else:
                if nums[i] - nums[i-1] == 1:
                    prev[i] = 2
                    expect_pos = False
                else:
                    prev[i] = 1
                    expect_pos = True
            
            max_len = max(max_len, prev[i])
        
        if max_len == 1:
            return -1
        return max_len

