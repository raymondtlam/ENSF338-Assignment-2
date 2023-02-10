import timeit
import matplotlib.pyplot as plt

def main():
    # Recursive Fibonacci Function
    def original_fib(n):
        if n == 0 or n == 1:
            return n
        else:
            return original_fib(n-1) + original_fib(n-2)

    # Memoized Fibonacci Function
    def optimized_fib(n, cache = {}):
        if n in cache:
            return cache[n]

        if n == 0 or n == 1:
            return n
        
        cache[n] = optimized_fib(n-1) + optimized_fib(n-2)
        return cache[n] 

    # Obtaining the x and y values for plot
    n_values = range(36) 
    slow_fib = [timeit.timeit(lambda: original_fib(n), number=1) for n in n_values]
    fast_fib = [timeit.timeit(lambda: optimized_fib(n), number=1) for n in n_values]

    # Creating plot
    fig, ax = plt.subplots()
    ax.plot(n_values, slow_fib)
    ax.plot(n_values, fast_fib)
    ax.legend(["Recursive Fibonacci Function", "Memoized Fibonacci Function"])
    plt.xlabel("n-th Fibonacci Term")
    plt.ylabel("Time to Return Value (s)")
    plt.title("Time Taken to Return the n-th Fibonacci Term")
    plt.show()

if __name__ == "__main__":
    main()
