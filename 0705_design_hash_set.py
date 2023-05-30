# you can find your own hash of the key calculation, idea is below
class MyHashSet:
    def __init__(self):
        self.hash_set = [0] * (10**6 + 1)
        
    def add(self, key: int) -> None:
        self.hash_set[key] = 1

    def remove(self, key: int) -> None:
        self.hash_set[key] = 0

    def contains(self, key: int) -> bool:
        return self.hash_set[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
