class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        majority = 0

        for num in nums:
            if majority == 0:
                res = num
            
            majority += 1 if res == num else -1
        return res
