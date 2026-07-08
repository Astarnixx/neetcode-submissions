class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left,right = 0,n-1
        maxamt = 0
        while left<=right:
            h = min(heights[left],heights[right])
            amt = (right-left)*h
            maxamt = max(amt, maxamt)
            if h == heights[left]:
                left+=1
            if h == heights[right]:
                right-=1
        return maxamt