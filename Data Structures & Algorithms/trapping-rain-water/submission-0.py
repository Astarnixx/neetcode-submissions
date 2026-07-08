class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        l,r = [0]*n, [0]*n
        l[0] = height[0]
        r[n-1] = height[n-1]
        for i in range(1,n):
            l[i] = max(l[i-1],height[i])
        for i in range(n-2,-1,-1):
            r[i] = max(r[i+1],height[i])
        amt = 0
        for i in range(n):
            amt += (min(l[i],r[i]) - height[i])
        return amt