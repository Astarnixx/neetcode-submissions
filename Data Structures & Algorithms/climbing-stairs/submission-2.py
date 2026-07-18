class Solution:
    def climbStairs(self, n: int) -> int:
        #Bottom Up - the total ways to reach step i is sum of ways to reach the prev 2 steps
        if n<=2:
            return n #If only 1/2 steps to climb, only 1/2 ways.
        dp = [-1]*(n+1) #dp array to track number of ways to reach step i
        dp[1],dp[2]=1,2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]