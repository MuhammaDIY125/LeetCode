class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        print(dp)
        dp[0] = dp[1] = 1
        print(dp)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp)
        return dp[n]

s1 = Solution()
n = 2
print(s1.climbStairs(n))