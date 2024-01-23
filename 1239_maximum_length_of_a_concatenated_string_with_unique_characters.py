class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr_dict = []
        for string in arr:
            occurences = defaultdict(int)
            for char in string:
                occurences[char] += 1
            arr_dict.append(occurences)

        memo = {}
        def backtracking(idx, state):
            if (idx, state) in memo:
                return memo[(idx, state)]

            if idx >= len(arr):
                return 0
            
            must_skip = False
            new_state = state
            for char in arr[idx]:
                base_idx = ord(char) - 97
                if (new_state >> base_idx) & 1 == 1:
                    must_skip = True
                    break
                
                new_state = new_state | (1 << base_idx)
            
            total = 0
            if not must_skip:
                total = len(arr[idx]) + backtracking(idx + 1, new_state)
            
            total = max(total, backtracking(idx + 1, state))
            memo[(idx, state)] = total
            return total
        
        state = 1 << 26
        return backtracking(0, state)
