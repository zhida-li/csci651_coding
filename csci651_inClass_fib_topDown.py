# https://leetcode.com/problems/fibonacci-number/description/
cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]


print(fib(30))
