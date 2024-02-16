class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count_map = defaultdict(int)
        for num in arr:
            count_map[num] += 1
        
        unsorted_count = []
        for num in count_map:
            unsorted_count.append((num, count_map[num]))
        
        sorted_count = sorted(unsorted_count, key=lambda x: x[1])
        curr_idx = 0
        while k > 0:
            _, freq = sorted_count[curr_idx]
            if freq > k:
                break

            if freq <= k:
                curr_idx += 1
                k -= freq

        return len(sorted_count) - curr_idx

