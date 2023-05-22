class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)

        for num in nums:
            hmap[num] += 1

        bucket = [[] for i in range(len(nums) + 1)]
        for key in hmap:
            frequency = hmap[key]
            bucket[frequency].append(key)
        
        res = []
        need = k
        for i in range(len(nums), -1, -1):
            if need == 0:
                break
            
            if bucket[i] == []:
                continue
            
            if need >= len(bucket[i]):
                res.extend(bucket[i])
                need -= len(bucket[i])
            else:
                res.extend(bucket[i][:need])
                need = 0

        return res


