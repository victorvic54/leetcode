class Solution:
    def sumOfDevices(self, row):
        devices = 0
        for num in row:
            if num == "1":
                devices += 1
        return devices

    def numberOfBeams(self, bank: List[str]) -> int:
        prev = None
        ans = 0
        for row in bank:
            devices = self.sumOfDevices(row)
            if devices == 0:
                continue
            
            if prev != None:
                ans += prev * devices
            
            prev = devices
        
        return ans

