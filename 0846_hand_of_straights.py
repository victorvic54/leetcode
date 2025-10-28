class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        key_idx = defaultdict(int)

        for card in hand:
            key_idx[card] += 1
        
        for key in key_idx:
            num = key_idx[key]
            if num <= 0:
                continue

            for idx in range(key, key + groupSize):
                key_idx[idx] -= num
                if key_idx[idx] < 0:
                    return False
        return True

"""
Time:
Sorting: O(n log n)
Removal of group: O(m × groupSize) = O(n)
However, since each card is effectively processed only a constant number of times (once per group it participates in),and the total number of cards is n, this is bounded by O(n) in practice.

Space:
O(n)
"""
