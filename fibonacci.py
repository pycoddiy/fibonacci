"""
The Ultimate Python - Fibonacci

Watch at https://www.youtube.com/@pycoddiy

The Ultimate Python is a new YouTube channel from @PyCodDIY covering different
aspects of performance programming with Python.

This file illustrates performance aspects of implementing the Fibonacci sequence for large numbers.
"""

from time import time


def fibonacci_recursive(n):
    """
    Recursive implementation (slowest)

    :param n: The order (index) of the Fibonacci number
    :return: The list of `n` first Fibonacci numbers
    """
    def _fib(n):
        if n in {0, 1}:
            return n
        else:
            return _fib(n - 1) + _fib(n - 2)

    return [_fib(k) for k in range(n + 1)]


def fibonacci_caching(n):
    """
    Efficient implementation using caching

    :param n: The order (index) of the Fibonacci number
    :return: The list of `n` first Fibonacci numbers
    """
    cache = {0: 0, 1: 1}  # Initial cache for F(0) and F(1)

    def _fib(n):
        if n not in cache:
            cache[n] = _fib(n - 1) + _fib(n - 2)
        return cache[n]

    return [_fib(k) for k in range(n + 1)]


N = 35
print("*** RECURSIVE IMPLEMENTATION  ***")
print(f"N={N}")
t1 = time()
seq = fibonacci_recursive(N)
t2 = time()
print(f"Elapsed time {t2 - t1:.3f} seconds")
print("First 10 elements:", seq[:10])


N = 300000
print("*** IMPLEMENTATION WITH CACHING ***")
print(f"N={N}")
t1 = time()
seq = fibonacci_caching(N)
t2 = time()
print(f"Elapsed time {t2 - t1:.3f} seconds")
print("First 10 elements:", seq[:10])
