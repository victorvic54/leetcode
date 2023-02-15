class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # without map, join, list
        for i in range(len(num) - 1, -1, -1):
            if not k:
                break
            k, num[i] = divmod(num[i] + k, 10)
            print(num)
        
        while k:
            k, a = divmod(k, 10)
            num = [a] + num
        return num


    # one-line answer
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return map(int, list(str(int(''.join(list(map(str, num)))) + k)))
