class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        self.result = 0
        self.memo = {}
        return self.backtracking(x, y, z, None)

    def backtracking(self, tmp_x, tmp_y, tmp_z, prev):
        if (tmp_x, tmp_y, tmp_z, prev) in self.memo:
            return self.memo[(tmp_x, tmp_y, tmp_z, prev)]

        res = 0
        if not prev or prev == "X":
            if tmp_y > 0:
                res = max(res, 2 + self.backtracking(tmp_x, tmp_y - 1, tmp_z, "Y"))

        if not prev or prev == "Y":
            if tmp_x > 0:
                res = max(res, 2 + self.backtracking(tmp_x - 1, tmp_y, tmp_z, "X"))

            if tmp_z > 0:
                res = max(res, 2 + self.backtracking(tmp_x, tmp_y, tmp_z - 1, "Z"))

        if not prev or prev == "Z":
            if tmp_x > 0:
                res = max(res, 2 + self.backtracking(tmp_x - 1, tmp_y, tmp_z, "X"))
            
            if tmp_z > 0:
                res = max(res, 2 + self.backtracking(tmp_x, tmp_y, tmp_z - 1, "Z"))

        self.memo[(tmp_x, tmp_y, tmp_z, prev)] = res
        return res
