class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remaining = defaultdict(int)
        for char in s:
            remaining[char] += 1
        
        seen = set()
        stack = []
        for char in s:
            remaining[char] -= 1
            if char in seen:
                continue

            while stack and char < stack[-1]:
                if remaining[stack[-1]] <= 0:
                    break

                seen.remove(stack[-1])
                stack.pop()

            seen.add(char)        
            stack.append(char)
        
        return "".join(stack)

# Time: O(n)
# Space: O(n)
