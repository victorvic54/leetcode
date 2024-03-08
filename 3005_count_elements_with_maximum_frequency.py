class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        max_freq = 0
        for num in nums:
            freq_map[num] += 1
            max_freq = max(max_freq, freq_map[num])
        
        nums_with_max_freq = 0
        for _, freq in freq_map.items():
            if freq == max_freq:
                nums_with_max_freq += 1
        
        return nums_with_max_freq * max_freq

