class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            tmp_arr = nums[i:i+3]
            if tmp_arr[-1] - tmp_arr[0] > k:
                return []
            ans.append(tmp_arr)
        return ans
