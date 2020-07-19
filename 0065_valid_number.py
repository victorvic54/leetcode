'''

DFA implementation: the DFA can be seen here:
https://github.com/victorvic54/SAP_intern/blob/master/DFA_is_valid_integer.jpeg

'''

class Solution:
    def isNumber(self, s: str) -> bool: 
        state = [
            {'blank': 0, 'sign': 1, 'digit':2, '.':3},  # 0
            {'digit':2, '.':3},                         # 1
            {'digit':2, '.':4, 'e':5, 'blank':8},       # 2
            {'digit':4},                                # 3
            {'digit':4, 'e':5, 'blank':8},              # 4
            {'sign':6, 'digit':7},                      # 5
            {'digit':7},                                # 6
            {'digit':7, 'blank':8},                     # 7
            {'blank':8}                                 # 8
        ]

        currentState = 0
        
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            elif c == ' ':
                c = 'blank'
            elif c in ['+', '-']:
                c = 'sign'
            
            if c not in state[currentState]:
                return False
            
            currentState = state[currentState][c]
            
        if currentState not in [2,4,7,8]:
            return False

        return True