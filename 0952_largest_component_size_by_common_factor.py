from collections import defaultdict
from collections import Counter

'''
Given an array example: [2,3,6,7,4,12,21,39]
1. I want to the prime factorization of each of the number below
'''
class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr


class Solution:
    def primes_set(self,n):
        for i in range(2, int(n ** (1/2))+1):
            if n % i == 0:
                return self.primes_set(n//i) | set([i])
        return set([n])

    def largestComponentSize(self, A):
        n = len(A)
        UF = DSU(n)
        primes = defaultdict(list)

        print(self.primes_set(21))
        for i, num in enumerate(A):
            pr_set = self.primes_set(num)
            for q in pr_set:
                primes[q].append(i)

        # print(primes)

        for _, indexes in primes.items():
            for i in range(len(indexes)-1):
                UF.union(indexes[i], indexes[i+1])

        result = [UF.find(i) for i in range(n)]
        return max(Counter(result).values())


sol = Solution()
arr = [2,3,6,7,4,12,21,39]
print(sol.largestComponentSize(arr))