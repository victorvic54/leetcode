class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_pointer = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and pop_pointer < len(popped) and stack[-1] == popped[pop_pointer]:
                stack.pop()
                pop_pointer += 1

        return pop_pointer == len(popped)


class MySolution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push_pointer = 0
        pop_pointer = 0

        stack = []
        history = set()
        
        while pop_pointer < len(popped):
            while push_pointer < len(pushed) and popped[pop_pointer] not in history:
                stack.append(pushed[push_pointer])
                history.add(pushed[push_pointer])
                push_pointer += 1

            if stack[-1] == popped[pop_pointer]:
                stack.pop()
                history.remove(popped[pop_pointer])
                pop_pointer += 1
            else:
                return False
        
        return True
