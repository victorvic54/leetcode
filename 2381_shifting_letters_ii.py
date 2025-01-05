class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_list = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            if direction == 0:
                shift_list[start] -= 1
                shift_list[end + 1] += 1
            else:
                shift_list[start] += 1
                shift_list[end + 1] -= 1

        base_char_ord = ord('a')
        counter = 0
        char_list = []
        for i in range(len(s)):
            counter += shift_list[i]
            adjusted_char = base_char_ord + (((ord(s[i]) + (counter % 26)) - base_char_ord) % 26)
            char_list.append(chr(adjusted_char))
        
        return "".join(char_list)

