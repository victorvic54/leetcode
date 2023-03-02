class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = chars[0]
        count = 0
        tmp_idx = 0
        
        i = 0 # <--
        while True: # try to imitate do while loop instead of normal (for char in chars) loop. Marked by <--
            if i < len(chars): # <--
                char = chars[i]
            
            if i == len(chars) or prev != char:  # <--
                chars[tmp_idx] = prev
                tmp_idx += 1

                if count > 1:
                    count_len = len(str(count))
                    for j in range(count_len):
                        chars[tmp_idx] = str(count)[j]
                        tmp_idx += 1

                if i == len(chars): # <--
                    break

                prev = char
                count = 1
            else:
                prev = char
                count += 1

            i += 1 # <--
        
        return tmp_idx

