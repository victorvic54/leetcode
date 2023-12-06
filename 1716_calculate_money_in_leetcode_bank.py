class Solution:
    def totalMoney(self, n: int) -> int:
        total_money = 0
        for i in range(n):
            total_money += (i // 7) + (i % 7) + 1
        
        return total_money
