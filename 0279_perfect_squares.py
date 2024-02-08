class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        ans = 0
        
        for num in all_nums:
            if num-1 in all_nums: # let the even lower number to catch up
                continue
                
            count = 1
            while num+count in all_nums:
                count += 1
            
            ans = max(ans, count)
            
        return ans


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        all_nums = set(nums)
        freq = {}
        visited = set()
        for num in nums:
            if num in visited:
                continue

            tmp_len = -1
            tmp_num = num
            while tmp_num in all_nums:
                visited.add(tmp_num)
                tmp_len += 1
                tmp_num -= 1
            
            tmp_num = num
            while tmp_num in all_nums:
                visited.add(tmp_num)
                tmp_len += 1
                tmp_num += 1
            
            ans = max(ans, tmp_len)
        return ans

