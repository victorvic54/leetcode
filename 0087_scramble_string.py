class Solution:
    def isScramble(self, s1, s2):
        self.memo = {}
        return self.scrambleHelper(s1, s2)

    def scrambleHelper(self, s1, s2):
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]

        if len(s1) != len(s2):
            return False
        
        if s1 == s2:
            return True
        
        if sorted(s1) != sorted(s2): # prunning
            return False
        
        for i in range(1, len(s1)):
            if (self.scrambleHelper(s1[:i], s2[:i]) and self.scrambleHelper(s1[i:], s2[i:])) or \
               (self.scrambleHelper(s1[:i], s2[-i:]) and self.scrambleHelper(s1[i:], s2[:-i])):
                self.memo[(s1, s2)] = True
                return True

            self.memo[(s1, s2)] = False

        return False
