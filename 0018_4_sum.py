'''

The bases case test (need to ignore) include:
1. If the updated list is less than the desire pairs or the desire pairs are less than 2
2. Since it is sorted, if my target I want is less than the smallest number in the current array (nums) times N_pairs
3. Since it is sorted, if my target I want is more than the biggest number in the current array (nums) times N_pairs

Next is the idea of 2 Sum

'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNSum(nums, target, N_pairs, tmp_result, result_list):
            if (len(nums) < N_pairs) or (N_pairs < 2) or (target < nums[0] * N_pairs) or (target > nums[-1] * N_pairs):
                return
                        
            if (N_pairs == 2):
                left, right = 0, len(nums) - 1
                
                while (left < right):
                    total = nums[left] + nums[right]
    
                    if (total == target):
                        result_list.append(tmp_result + [nums[left], nums[right]])

                        while (left < right) and (nums[left] == nums[left + 1]):
                            left += 1

                        while (left < right) and (nums[right - 1] == nums[right]):
                            right -= 1

                        left += 1
                        right -= 1
                    elif (total < target):
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(len(nums) - N_pairs + 1):                 
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNSum(nums[i+1:], target - nums[i], N_pairs - 1, tmp_result + [nums[i]], result_list)

                                                                        
        result_list = []                                          
        nums = sorted(nums)
        N_pairs = 4

        findNSum(nums, target, N_pairs, [], result_list)
        
        return result_list