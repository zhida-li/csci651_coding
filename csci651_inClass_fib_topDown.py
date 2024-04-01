# https://leetcode.com/problems/fibonacci-number/description/
memo = {}

def fib_top_down(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    f = fib_top_down(n-1) + fib_top_down(n-2)
    memo[n] = f
    return memo[n]



print(fib_top_down(30))
