class Solution:
    def climbStairs(self, n: int) -> int:
        #Bottom Up - the total ways to reach step i is sum of ways to reach the prev 2 steps
        if n<=2:
            return n #If only 1/2 steps to climb, only 1/2 ways.
        prev2,prev1=1,2
        for i in range(3,n+1):
            curi = prev1+prev2
            prev2=prev1
            prev1=curi
        return prev1