class RandomizedSet:
    def __init__(self):
        self.none_counter = 0
        self.value_dict = {}
        self.value_arr = []

    def insert(self, val: int) -> bool:
        if val in self.value_dict:
            return False

        self.value_dict[val] = len(self.value_arr)
        self.value_arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_dict:
            return False
        
        idx = self.value_dict[val]
        self.value_dict[self.value_arr[self.none_counter]] = idx
        self.value_arr[idx] = self.value_arr[self.none_counter]

        self.value_arr[self.none_counter] = None
        del self.value_dict[val]

        self.none_counter += 1
        return True

    def getRandom(self) -> int:
        target_idx = random.randint(self.none_counter, len(self.value_arr) - 1)
        return self.value_arr[target_idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
