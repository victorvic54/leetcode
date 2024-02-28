"""
Idea is to use linkedlist to maintain O(1) because deletion in a list took O(n)
"""
class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.first = Node(None, None)
        self.last = Node(None, None)
        self.first.next = self.last
        self.last.prev = self.first

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self, node):
        prev_node = self.last.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.last
        self.last.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = Node(key, value)
        self.insert(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            first_node = self.first.next
            self.remove(first_node)
            del self.cache[first_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
