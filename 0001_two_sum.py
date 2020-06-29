'''
Create an inversion from the target to each of the list component.
Check using hashset whether the number exists
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()
        
        for i in range(len(nums)):
            wanted = target - nums[i]
            
            if wanted not in my_dict:
                my_dict[nums[i]] = i
            else:
                return [my_dict[wanted], i]
            