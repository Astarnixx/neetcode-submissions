class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def checkChar(string):
            mp=[0]*256
            n=len(string)
            for i in range(n):
                mp[ord(string[i])] += 1
            return mp
        return True if checkChar(s)==checkChar(t) else False
        