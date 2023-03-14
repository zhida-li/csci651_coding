# https://leetcode.com/problems/n-th-tribonacci-number/description/
cache = {}

def tribonacci(n):
    if n == 0:
        return 0
    
    if n==1 or n==2:
        return 1
    
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    # from dp[3] to dp[n]
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    return dp[n]
    

print(tribonacci(25))
