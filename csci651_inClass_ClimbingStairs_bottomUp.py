# https://leetcode.com/problems/climbing-stairs/description/
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0]*(n+1)
    # dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    # from n = 3
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]


print(climbStairs(5))
