class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        queue = collections.deque([0]*26)

        for c in s:
            queue[ord(c) - ord('a')] += 1

        for _ in range(t):
            z = queue.pop()
            queue.appendleft(z)

            # z --> ab  b += freq of z
            queue[1] += z
        
        return sum(queue) % (10**9 + 7)


    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        counter = Counter(s)

        while t:
            z_count = counter['z']
            for char in [chr(c) for c in range(ord('y'), ord('a') - 1, -1)]:
                counter[chr(ord(char) + 1)] = counter[char]

            counter['a'] = z_count
            counter['b'] = (counter['b'] + z_count) % MOD
            t -= 1
        
        result = 0
        for _, count in counter.items():
            result = (result + count) % MOD
        return result

