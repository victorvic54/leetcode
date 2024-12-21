"""
Let N be the length of s and K be the number of unique characters in s
  Time complexity = O(N * log(K))
  Space Complexity = O(K)
"""
class OrderedAlphabet:
    def __init__(self, letter, count):
        self.letter = letter
        self.count = count
    
    def __lt__(self, other):
        return self.letter > other.letter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        word_dict = defaultdict(int)
        for char in s:
            word_dict[char] += 1
        
        alphabet_list = []
        for char in word_dict:
            heapq.heappush(alphabet_list, OrderedAlphabet(char, word_dict[char]))
        
        results = []
        while alphabet_list:
            curr_alphabet = heapq.heappop(alphabet_list)
            char_count = min(curr_alphabet.count, repeatLimit)
            results.extend([curr_alphabet.letter] * char_count)

            if alphabet_list and curr_alphabet.count - char_count > 0:
                next_alphabet = heapq.heappop(alphabet_list)
                results.extend([next_alphabet.letter] * 1)
                if next_alphabet.count - 1 > 0:
                    heapq.heappush(alphabet_list, OrderedAlphabet(next_alphabet.letter, next_alphabet.count - 1)) 
                heapq.heappush(alphabet_list, OrderedAlphabet(curr_alphabet.letter, curr_alphabet.count - char_count))

        return "".join(results)

