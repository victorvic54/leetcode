class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        nett_gas = []
        for i in range(len(gas)):
            nett_gas.append(gas[i] - cost[i])
        
        if sum(nett_gas) < 0:
            return -1

        tmp_sum = 0
        candidate = 0
        for i in range(len(nett_gas)):
            tmp_sum += nett_gas[i]
            if tmp_sum < 0:
                tmp_sum = 0
                candidate = i + 1

        return candidate

# Time: O(n)
# Space: O(n) -> can be improved to O(1)
