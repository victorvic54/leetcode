'''

Things to note:
1. You need to sort for 3Sum ++ problem because it is at least n^2 (which is different from 2Sum)
2. You dont need to continue checking if (nums[i] > 0)
3. You want to remove duplicates by checking at line 19

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        
        for i in range(len(nums) - 2):
            if (nums[i] > 0):
                break
            
            if (i > 0 and nums[i] == nums[i-1]):
                continue

            left = i + 1
            right = len(nums) - 1
            
            while (left < right):
                total = nums[i] + nums[left] + nums[right]
                
                if (total < 0):
                    left += 1
                elif (total > 0):
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                
                    while (left < right) and (nums[left] == nums[left + 1]):
                        left += 1

                    while (left < right) and (nums[right - 1] == nums[right]):
                        right -= 1

                    left += 1
                    right -= 1
        
        return result