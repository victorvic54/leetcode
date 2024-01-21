class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        histories = []
        min_num = nums[0]
        max_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1].bit_count() == nums[i].bit_count():
                min_num = min(min_num, nums[i])
                max_num = max(max_num, nums[i])
            else:
                histories.append((min_num, max_num))
                min_num = nums[i]
                max_num = nums[i]
            
            if i == len(nums) - 1:
                histories.append((min_num, max_num))
        
        for i in range(1, len(histories)):
            prev_min_num, prev_max_num = histories[i-1]
            next_min_num, next_max_num = histories[i]
            if prev_max_num > next_min_num:
                return False
        
        return True

