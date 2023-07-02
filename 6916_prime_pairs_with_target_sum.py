class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        # Generate all primes up to n using Sieve of Eratosthenes
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1

        prime_pairs = []
        for i in range(2, n // 2 + 1):
            if primes[i] and primes[n - i]:
                prime_pairs.append([i, n - i])

        return prime_pairs

