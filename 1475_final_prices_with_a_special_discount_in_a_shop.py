"""
Let n be the length of the input array prices.
  Time complexity: O(n)
  Space complexity: O(n)
"""
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = deque([prices[-1]])
        result = prices.copy()

        for i in range(len(prices) - 2, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()

            if stack:
                result[i] = prices[i] - stack[-1]
            
            stack.append(prices[i])
        
        return result

