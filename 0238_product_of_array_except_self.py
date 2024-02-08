# brute force use division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZero = 0
        totalMult = 1
        for num in nums:
            if num != 0:
                totalMult = totalMult * num
            else:
                numZero += 1
        
        ans = []
        for num in nums:
            if num == 0:
                if numZero == 1:
                    ans.append(totalMult)
                elif numZero > 1:
                    ans.append(0)
            else:
                if numZero >= 1:
                    ans.append(0)
                else:
                    ans.append(int(totalMult / num))
        return ans


"""
Solution without division, better solution
[1,2,3,4]
prefix_mult = [1,2,6,24]
suffix_mult = [24,24,12,4]
ans = [24,12,8,6] <--- can you see the pattern

Further optimized to:
prefix_mult = [ -, 1, 1, 2, 6,24]
suffix_mult = [24,24,12, 4, 1, -]
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [None] * len(nums)
        right_arr = [None] * len(nums)
        answer = [None] * len(nums)

        left_arr[0] = 1
        right_arr[-1] = 1

        for i in range(1, len(nums)):
            left_arr[i] = left_arr[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right_arr[i] = right_arr[i+1] * nums[i+1]

        for i in range(len(nums)):
            answer[i] = left_arr[i] * right_arr[i]

        return answer


"""
Elegant solution without division
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res

