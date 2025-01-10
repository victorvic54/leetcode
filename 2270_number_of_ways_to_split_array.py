# nums = [10, 4, -8, 7]
# prefix_arr = [10, 14, 6, 13]
# suffix_arr = [13, 3, -1, 7]
#
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        prefix_sum = 0
        num_valid_split = 0
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            if prefix_sum >= total_sum - prefix_sum:
                num_valid_split += 1
        return num_valid_split

