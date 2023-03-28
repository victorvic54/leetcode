# greedy algorithm using DP
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.days = days
        self.dp = [0] * (len(days) + 1)

        for i in range(1, len(self.dp)):
            self.dp[i] = min(
                self.get_lowest_cost(i, 1) + costs[0],
                self.get_lowest_cost(i, 7) + costs[1],
                self.get_lowest_cost(i, 30) + costs[2],
            )
        return self.dp[-1]
    
    # remember curr_idx is index + 1 for self.dp but not for self.days
    def get_lowest_cost(self, curr_idx, days_before):
        curr_day = self.days[curr_idx - 1]

        while curr_idx > 0:
            curr_idx -= 1
            if curr_day - self.days[curr_idx - 1] >= days_before:
                break
        
        return self.dp[curr_idx]]

