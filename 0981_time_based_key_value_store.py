class TimeMap:
    def __init__(self):
        self.time_values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_values[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        time_value_list = self.time_values[key]
        tuple_idx = self._bisect_right(time_value_list, timestamp) - 1
        if tuple_idx < 0:
            return ""
        return time_value_list[tuple_idx][1]
    
    def _bisect_right(self, arr, target):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= target:
                left = mid + 1
            else:
                right = mid
        return left

# Time: O(log n) per get, O(1) per set
# Space: O(n) overall per key.

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
