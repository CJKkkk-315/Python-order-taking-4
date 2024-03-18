class Solution:
    def minDays(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2 or n == 3:
            return 2
        dp = [99999999 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 2
        for i in range(4,n+1):
            dp[i] = min(dp[i-1]+1,dp[i])
            if i % 2 == 0:
                dp[i] = min(dp[i],dp[i//2]+1)
            if i % 3 == 0:
                dp[i] = min(dp[i],dp[i-2*(i//3)]+1)
        return dp[-1]

s = Solution()
print(s.minDays(182))