'''
Things to take note here: "consecutive"
Using the knowledge of previous result for the use of current result.
'''
class StockSpanner:
    def __init__(self):
        self.data = []
        
    def next(self, price: int) -> int:
        s = 1
        while self.data and self.data[-1][0] <= price:
            s += self.data[-1][1]
            self.data.pop()
        self.data.append((price, s))
        return s


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
