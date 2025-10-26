class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def backtracking(idx, left):
            if (idx, left) in memo:
                return memo[(idx, left)]

            if left == 0:
                return 0
            
            if left < 0:
                return float('inf')
            
            if idx >= len(coins):
                return float('inf')
            
            min_counter = float('inf')
            min_counter = min(min_counter, backtracking(idx + 1, left))
            min_counter = min(min_counter, 1 + backtracking(idx, left - coins[idx]))
            memo[(idx, left)] = min_counter
            return min_counter

        min_counter = backtracking(0, amount)
        return min_counter if min_counter != float('inf') else -1
    
# Time: O(n * amount)
# Space: O(n * amount)


    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + ([float('inf')] * (amount))
        
        for i in range(1, amount + 1):
            if (i in coins):
                dp[i] = 1
            else:
                for j in range(len(coins)):
                    if (coins[j] > i):
                        continue
                    else:
                        dp[i] = min(dp[i], dp[i-coins[j]] + 1)
                
        if (dp[-1] == float('inf')):
            return -1
        else:
            return dp[-1]


# =============================================================
def coin_change_greedy(amt, coins):
    num_coins = 0

    for i in range(len(coins) - 1, -1, -1):
        num_coins += (amt // coins[i])
        amt = amt % coins[i]

    if (amt != 0):
        return float('inf')
    
    return num_coins


def coin_change_rec1(amt, k, coins):
    if (amt == 0):
        return 0
    
    if (amt < 0 or (k < 0 and amt > 0)):
        return float('inf')

    return min(coin_change_rec1(amt, k-1, coins), 1 + coin_change_rec1(amt-coins[k], k, coins))


def coin_change_rec2(amt, coins):
    if (amt == 0):
        return 0
    
    tmp = float('inf')
    for coin in coins:
        if (amt - coin >= 0):
            tmp = min(tmp, 1 + coin_change_rec2(amt - coin, coins))
    
    return tmp


def coin_change_memo(amt, coins):
    if (amt == 0):
        return 0
    
    if (dp[amt]):
        return dp[amt]

    tmp = float('inf')
    for coin in coins:
        if (amt - coin >= 0):
            tmp = min(tmp, 1 + coin_change_memo(amt - coin, coins))
    
    dp[amt] = tmp
    return dp[amt]


arr = [1,4,7,13,28,52,91,365]

# for i in range(1, 100):
#     dp = [0] + ([None] * (i))
#     a = coin_change_memo(i, arr)
#     b = coin_change_rec1(i, len(arr) - 1, arr)
#     if (a != b):
#         print("M")

# print(coin_change_rec1(i, len(arr) - 1, arr))
# print(coin_change_rec2(i, arr))
