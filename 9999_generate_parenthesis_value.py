from pprint import pprint

def diffWaysToCompute(n, k, t, x, M):
    dp = [[[] for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp[i][i].append(int(x[i]))
    
    # nn indicates the result of possible values of parenthesis at nn-th point 
    for nn in range(2, n+1):
        # (i, i+j-1) below indicates which pair to be evaluate first (which is the recursive assumption)
        # (i+j, i+nn-1) below indicates another pair that needs to be evaluate first (which is another recursive assumption)
        for i in range(n+1-nn):
            for j in range(1, nn):
                # ax and ay below are possible values that range betweem (1...k) and no duplicates
                for ax in dp[i][i+j-1]:
                    for ay in dp[i+j][i+nn-1]:
                        dp[i][i+nn-1] += [M[ax-1][ay-1]]
                        dp[i][i+nn-1] = list(set(dp[i][i+nn-1]))

    # print(dp[0][n-1])
    return (t in dp[0][n-1])


M = [[1,3,3], [1,1,2], [3,3,3]]
x = "2221"
n = len(x)
k = len(M)
t = 3

print(diffWaysToCompute(n, k, t, x, M))