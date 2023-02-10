import json
import sys
import timeit
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)

def func1(arr, low, high):
        if low < high:
            pi = func2(arr, low, high)
            func1(arr, low, pi-1)
            func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[end//2]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def main():
    # Load JSON file
    with open('ex2.json') as f:
        d = json.load(f)

    # Initialize list for number of entries and times
    n = []
    times = []

    # Iterate through list of list
    for sortlist in d:
        length = len(sortlist)
        n.append(length)
        times.append(timeit.timeit(lambda: func1(sortlist, 0, length-1), number = 1))
    
    # Creating plot
    fig, ax = plt.subplots()
    ax.plot(n, times)
    plt.xlabel("Number of Terms in List")
    plt.ylabel("Time to Sort Array (s)")
    plt.title("Time Taken for QuickSort to Sort n Terms In An Array")
    plt.show()

if __name__ == "__main__":
    main()
