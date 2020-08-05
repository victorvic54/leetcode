'''

We need lru_cache or memoization because we might have passed
1. self.isInterleave(s1[1:], s2, s3[1:])
2. self.isInterleave(s1, s2[1:], s3[1:])

which is the same as
1. self.isInterleave(s1, s2[1:], s3[1:])
2. self.isInterleave(s1[1:], s2, s3[1:])

So there is duplication in calculation

'''

class Solution:
    @lru_cache()
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not (s1 or s2):
            if (not s3):
                return True
        elif (not s1):
            if (s2 == s3):
                return True
        elif (not s2):
            if (s1 == s3):
                return True
        else:
            if (s1[0] == s3[0] and s2[0] == s3[0]):
                return self.isInterleave(s1[1:], s2, s3[1:]) or \
                        self.isInterleave(s1, s2[1:], s3[1:])
            elif (s1[0] == s3[0]):
                return self.isInterleave(s1[1:], s2, s3[1:])
            elif (s2[0] == s3[0]):
                return self.isInterleave(s1, s2[1:], s3[1:])
        
        return False


    # Lets break down lru_cache into visited and make it iterative
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c, l = len(s1), len(s2), len(s3)

        if r+c != l:
            return False

        stack = [(0, 0)]
        visited = set((0, 0))

        while stack:
            x, y = stack.pop()

            if x+y == l:
                return True

            if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
                stack.append((x+1, y))
                visited.add((x+1, y))

            if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
                stack.append((x, y+1))
                visited.add((x, y+1))

        return False
    
    
    # Dynamic programming
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c, l= len(s1), len(s2), len(s3)
        
        if r+c != l:
            return False
        
        dp = [[True] * (c+1) for _ in range(r+1)]
        
        for i in range(1, r+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
            
        for j in range(1, c+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, r+1):
            for j in range(1, c+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                           (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]