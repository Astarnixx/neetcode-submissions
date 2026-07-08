class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        t=list(s)
        s=list(s)
        start=0
        end=len(s)-1
        while start<=end:
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1
        return True if t==s else False
