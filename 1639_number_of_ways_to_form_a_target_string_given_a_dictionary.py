"""
DP Solution

      0  1  2  3
a -> [1, 1, 0, 2]
b -> [1, 1, 1, 1]
c -> [1, 1, 2, 0]

   -  0  1  2  3 
-  1  0  0  0  0
a  0  0  0  0  0
b  0  0  0  0  0
a  0  0  0  0  0
"""
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        alphabet = 26
        mod = 1000000007

        target_len = len(target)
        word_len = len(words[0])
        word_dict = [[0] * word_len for _ in range(alphabet)]
        for j in range(word_len):
            for word in words:
                word_dict[ord(word[j]) - ord('a')][j] += 1

        dp = [[0] * (word_len + 1) for _ in range(target_len + 1)]
        dp[0][0] = 1
        for i in range(target_len + 1):
            for j in range(word_len):
                if i < target_len:
                    dp[i + 1][j + 1] += (word_dict[ord(target[i]) - ord('a')][j] * dp[i][j])
                    dp[i + 1][j + 1] %= mod

                dp[i][j + 1] += dp[i][j]
                dp[i][j + 1] %= mod
        return dp[target_len][word_len]

"""
Backtracking + Memoization
"""
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        dict_list = [defaultdict(int) for i in range(len(words[0]))]
        for word in words:
            for i in range(len(word)):
                dict_list[i][word[i]] += 1
        
        memo = {}
        def backtracking(idx, fulfilled_idx):
            if (idx, fulfilled_idx) in memo:
                return memo[(idx, fulfilled_idx)]

            if fulfilled_idx >= len(target):
                return 1

            if idx >= len(words[0]):
                return 0
            
            total_ways = 0
            wanted_letter = target[fulfilled_idx]
            if wanted_letter in dict_list[idx]:
                total_ways += dict_list[idx][wanted_letter] * backtracking(idx + 1, fulfilled_idx + 1)
            total_ways += backtracking(idx + 1, fulfilled_idx)
            memo[(idx, fulfilled_idx)] = total_ways
            return total_ways
        
        MOD = 10**9 + 7
        return backtracking(0, 0) % MOD



"""
TLE Solution Backtracking + Memoization for MySolution

               a b c
0 -> [a, b, c] 1 1 1
1 -> [a, b, c] 1 1 1
2 -> [b, c, c] 0 1 2
3 -> [b, a, a] 2 1 0
"""
class MySolution:
    def numWays(self, words: List[str], target: str) -> int:
        self.MOD = (10 ** 9) + 7
        self.ALPHABET = 26

        self.word_dict = [[0] * self.ALPHABET for _ in range(len(words[0]))]
        self.target = target
        self.memo = {}

        for word in words:
            for i in range(len(word)):
                char_idx = ord(word[i]) - ord('a')
                self.word_dict[i][char_idx] += 1

        return self.get_total_ways(0, 0)

    def get_total_ways(self, idx, target_idx):
        if idx >= len(self.word_dict):
            return 0

        if (idx, target_idx) in self.memo:
            return self.memo[(idx, target_idx)]

        result = 0
        for i in range(idx, len(self.word_dict)):
            targeted_word_idx = ord(self.target[target_idx]) - ord('a')
            if self.word_dict[i][targeted_word_idx] == 0:
                continue
            
            tmp_result = self.word_dict[i][targeted_word_idx]
            if target_idx + 1 < len(self.target):
                next_result = self.get_total_ways(i + 1, target_idx + 1)
                tmp_result = tmp_result * next_result
                self.memo[(i + 1, target_idx + 1)] = next_result

            result = (result + tmp_result) % self.MOD
        
        return result

