N = 10
d = 4
n = 5
a = [3,4,6,8,10]
c = [2,5,2,5,1]

dp = [float('inf')] * (N+1)
dp[0] = 0

for i in range(len(a)):
    local_min = float('inf')
    hotel = a[i]

    for j in range(hotel-1, hotel-d-1, -1):
        if (j < 0):
            break
        else:
            local_min = min(local_min, dp[j] + c[i])

    dp[hotel] = local_min

print(dp)

