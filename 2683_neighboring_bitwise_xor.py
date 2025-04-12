class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        for initial_num in range(1):
            num = initial_num
            for i in range(len(derived)):
                if i == len(derived) - 1:
                    if initial_num == derived[i] ^ num:
                        return True

                # original[i + 1] = derived[i] ⊕ original[i]
                num = derived[i] ^ num
        
        return False


# original[i + 1] = derived[i] ⊕ original[i]
# original[i + 2] = derived[i+1] ⊕ (derived[i] ⊕ original[i])
# original[i + 3] = derived[i+2] ⊕ (derived[i+1] ⊕ (derived[i] ⊕ original[i]))
# ...
# original[i] = derived[i+2] ⊕ (derived[i+1] ⊕ (derived[i] ⊕ original[i]))
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0

