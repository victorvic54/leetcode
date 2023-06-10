class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        dct = defaultdict(list)
        for i in range(m):
            num = 0
            for x in grid[i]: # convert into binary in base 10
                num *= 2
                num += x
            dct[num].append(i)
        ls = list(dct.keys())
        k = len(ls)
        
        if 0 in ls:
            return [dct[0][0]]
        
        # an observation here is that if there are no two rows that can fulfill floor(k/2),
        # it will not be fulfilled by any additional number of rows you add into it
        for i in range(k):
            for j in range(i+1, k):
                if ls[i]&ls[j] == 0:
                    return sorted([dct[ls[i]][0], dct[ls[j]][0]])
        return []

