class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        max_num = -1
        for key, value in counter.items():
            if key == value:
                max_num = max(max_num, key)
        return max_num

