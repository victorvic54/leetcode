class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        suffix = [0]*n
        for i in range(n-1, 0, -1):  # iterate until 0 so that don't consider the case of removing everything
            if i == n-1 or nums[i] < nums[i+1]: 
                ans += 1
                suffix[i] = nums[i]
            else:
                break

        for i, _ in enumerate(nums): 
            if i == 0 or nums[i-1] < nums[i]:
                if i < n-1: # don't consider the case of removing everything
                    ans += 1

                # on why i + 2, its just because of how bisect_right works
                # bisect_right will always remove the right most index (from the left) you pass to it
                #
                # remember that the following logic is to remove **at least one element** in between because
                # removing all left / all right has been covered above.
                #
                # given [9, 3, 5, 2, 6, 7, 8] and i=0 => bisect_right(suffix, 9, 2) will return 7 where n - k = 0,
                # means cannot remove anything in between index 0 and index 7
                #
                # given [1, 2, 3, 4, 5] and i=0 => bisect_right(suffix, 1, 2) will return 2 where n - k = 3,
                # because we can remove to [1, 3, 4, 5], [1, 4, 5], [1, 5]
                k = bisect_right(suffix, nums[i], i+2)
                ans += max(0, n - k)
            else:
                break

        # if we remove everything
        return ans+1
