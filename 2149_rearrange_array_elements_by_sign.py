class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_pointer = 0
        neg_pointer = 0
        ans = []
        for i in range(len(nums)):
            if i % 2 == 0:
                while nums[pos_pointer] < 0:
                    pos_pointer += 1
                ans.append(nums[pos_pointer])
                pos_pointer += 1
            else:
                while nums[neg_pointer] > 0:
                    neg_pointer += 1
                ans.append(nums[neg_pointer])
                neg_pointer += 1

        return ans

