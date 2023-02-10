def optimized_fib(n,cache = {}):
    if n in cache:
        return cache[n]

    if n == 0 or n == 1:
        return n
        
    cache[n] = optimized_fib(n-1) + optimized_fib(n-2)
    return cache[n] 
