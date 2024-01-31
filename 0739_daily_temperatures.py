class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0] * len(temperatures)
        for currDay, currTemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < currTemp:
                prevDay = stack.pop()
                res[prevDay] = currDay - prevDay
            stack.append(currDay)
        return res


class MySolution:
    def bisect_right(self, ls, target):
        left = 0
        right = len(ls)
        while left < right:
            mid = (left + right) // 2
            if ls[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperature_map = defaultdict(list)
        for i in range(len(temperatures)):
            temperature_map[temperatures[i]].append(i)

        ans = []
        for i in range(len(temperatures)):
            # opt: can do a check if yesterday temp is the same as today temp, can use last result
            curr_temp = temperatures[i] 
            next_temp_idx = float('inf')

            for temp in temperature_map:
                if curr_temp >= temp:
                    continue
                
                position = self.bisect_right(temperature_map[temp], i)
                if position >= len(temperature_map[temp]):
                    continue
                
                next_temp_idx = min(next_temp_idx, temperature_map[temp][position] - i)
                if next_temp_idx == 1:
                    break
            
            if next_temp_idx == float('inf'):
                ans.append(0)
            else:
                ans.append(next_temp_idx)
        
        return ans

