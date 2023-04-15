class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for i in range(n + 1)]

        for i in range(1, n + 1):
            for coins in range(0, k + 1):
                current_sum = 0
                for current_coins in range(0, min(len(piles[i - 1]), coins) + 1):
                    if current_coins > 0:
                        current_sum += piles[i - 1][current_coins - 1]
                    dp[i][coins] = max(dp[i][coins], current_sum + dp[i - 1][coins - current_coins])
        return dp[n][k]


# Time limit exceeded, wrong approach (here I approach from left to right of the piles, should be from top to bottom for each pile)
class MySolution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        self.piles = piles
        self.memo = {}
        return self.get_max_value([0] * len(piles), k)


    def get_max_value(self, tmp_piles_idx, picks_left):
        if picks_left == 0:
            return 0

        if (picks_left, tuple(tmp_piles_idx)) in self.memo:
            return self.memo[(picks_left, tuple(tmp_piles_idx))]

        final_result = 0
        for i in range(len(tmp_piles_idx)):
            if tmp_piles_idx[i] >= len(self.piles[i]):
                continue

            tmp_idx = tmp_piles_idx[i]
            tmp_piles_idx[i] += 1
            final_result = max(final_result, self.piles[i][tmp_idx] + self.get_max_value(tmp_piles_idx, picks_left - 1))
            tmp_piles_idx[i] -= 1

        self.memo[(picks_left, tuple(tmp_piles_idx))] = final_result
        return final_result

