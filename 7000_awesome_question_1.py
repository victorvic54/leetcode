"""
Shopback interview question:

Input : n = 5 m = 3
        a = 0, b = 1, k = 100
        a = 1, b = 4, k = 100
        a = 2, b = 3, k = 100
Output : 200
Explanation:
Initially array = {0, 0, 0, 0, 0}

After first operation:
array = {100, 100, 0, 0, 0}
After second operation:
array = {100, 200, 100, 100, 100}
After third operation:
array = {100, 200, 200, 200, 100}

Maximum element after m operations is 200.

Input : n = 4 m = 3
        a = 1, b = 2, k = 603
        a = 0, b = 0, k = 286
        a = 3, b = 3, k = 882
Output : 882
Explanation:
Initially array = {0, 0, 0, 0}

After first operation:
array = {0, 603, 603, 0}
After second operation:
array = {286, 603, 603, 0}
After third operation:
array = {286, 603, 603, 882}

Maximum element after m operations is 882.
"""

def findMax(n, m, a, b, k):
    arr = [0] * (n + 1)
     
    for i in range(m):
        lowerbound = a[i]
        upperbound = b[i]
         
        arr[lowerbound] += k[i]
        arr[upperbound + 1] -= k[i]
         
    continuous_sum = 0
    res = float('-inf')
         
    for i in range(n):
        continuous_sum += arr[i]
        res = max(res, continuous_sum)

    return res
     
n = 5
a = [0, 1, 2]
b = [1, 4, 3]
k = [100, 100, 100]
 
m = len(a)
print("Maximum value after 'm' operations is", findMax(n, m, a, b, k))

