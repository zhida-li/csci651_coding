# https://leetcode.com/problems/house-robber/description/
from functools import cache

def rob(nums):
    """Use cache"""
    n = len(nums)
    if n == 1:
        return nums[0]

    @cache

    def dp(i: int) -> int:
        if i < 0:
            return 0
        # rob current house: nums[i] - dp(i-2)
        # not rob, check previous house: dp(i-1)
        return max(nums[i] + dp(i-2),
                  dp(i-1))
    
    return dp(len(nums)-1)  

    """bottom-up dp"""
    """
    if len(nums) == 1:
        return nums[0]
    
    dp = [0]*len(nums)  # last index n-1
    n = len(nums)
    
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])

    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i-2],
                   dp[i-1])
    
    return dp[n-1]  # or dp[-1]
    """

"""
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""
print(rob([2,7,9,3,1]))
