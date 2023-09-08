"""
The Ultimate Python - Fibonacci

Watch at https://www.youtube.com/@pycoddiy

The Ultimate Python is a new YouTube channel from @PyCodDIY covering different
aspects of performance programming with Python.

This file illustrates performance aspects of implementing the Fibonacci sequence for large numbers.
"""

from time import time
import numpy as np


def fibonacci_recursive(n):
    """
    Recursive implementation (slowest)

    :param n: The order (index) of the Fibonacci number
    :return: The list of `n` first Fibonacci numbers
    """
    def _fib(m):
        if m in {0, 1}:
            return m
        else:
            return _fib(m - 1) + _fib(m - 2)

    return [_fib(k) for k in range(n + 1)]


def fibonacci_caching(n):
    """
    Efficient implementation using caching

    :param n: The order (index) of the Fibonacci number
    :return: The list of `n` first Fibonacci numbers
    """
    cache = {0: 0, 1: 1}  # Initial cache for F(0) and F(1)

    def _fib(m):
        if m not in cache:
            cache[m] = _fib(m - 1) + _fib(m - 2)
        return cache[m]

    return [_fib(k) for k in range(n + 1)]


def fibonacci_numpy(n):
    """
    Efficient implementation using NumPy

    :param n: The order (index) of the Fibonacci number
    :return: The NumPy array of `n` first Fibonacci numbers
    """
    fib = np.empty(n + 1, dtype=float)
    fib[0] = 0
    fib[1] = 1

    for k in range(2, n + 1):
        fib[k] = fib[k - 1] + fib[k - 2]

    return fib


def fibonacci_yield(n):
    """
    Efficient implementation using `yield` sequencing

    :param n: The order (index) of the Fibonacci number
    :return: The sequence of `n` first Fibonacci numbers
    """
    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b


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


N = 1000
print("*** IMPLEMENTATION WITH NUMPY ***")
print(f"N={N}")
t1 = time()
seq = fibonacci_numpy(N)
t2 = time()
print(f"Elapsed time {t2 - t1:.3f} seconds")
print("First 10 elements:", seq[:10])


N = 300000
print("*** IMPLEMENTATION WITH YIELD ***")
print(f"N={N}")
t1 = time()
seq = list(fibonacci_yield(N))
t2 = time()
print(f"Elapsed time {t2 - t1:.3f} seconds")
print("First 10 elements:", seq[:10])
