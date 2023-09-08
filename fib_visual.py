"""
The Ultimate Python - Fibonacci

Watch at https://www.youtube.com/@pycoddiy

The Ultimate Python is a new YouTube channel from @PyCodDIY covering different
aspects of performance programming with Python.

BONUS! This file visualizes the Fibonacci recurrence as a series of growing squares in a spiral.
The Matplotlib package is used for visualization.
"""

import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt


def fibonacci(n):
    """
    The Fibonacci number of the order `n`, `F(n)`

    :param n: The order (index) of the Fibonacci number
    :return: The NumPy array of `n` first Fibonacci numbers
    """
    fib = np.empty(n + 1, dtype=float)
    fib[0] = 0
    fib[1] = 1

    for k in range(2, n + 1):
        fib[k] = fib[k - 1] + fib[k - 2]

    return fib


def plot_spiral(n):
    """
    Plots Fibonnaci squares and draws Fibonacci spiral

    :param n: The order (index) of the Fibonacci number
    :return: None
    """
    seq = fibonacci(n)  # Get Fibonacci sequence as NumPy array

    x = y = 0.0  # Bottom-left corner of the initial square

    # Boundaries of the plot axes
    xmin = ymin = 0.0
    xmax = ymax = 0.0

    # The list of Fibonacci squares
    squares = []

    fk = fk1 = 0.0  # Boundary condition F(0) = 0, F(-1) = 0

    # Construct tiled squares
    for k in range(1, n + 1):
        fk, fk1, fk2 = float(seq[k]), fk, fk1  # F(k), F(k-1), F(k-2)

        dx = dy = 0.0  # Position of the k-th square relative to the previous one

        di = k & 3  # Determine direction of the square tiling (0 - right, 1 - up, 2 - left, 3 - down)
        if di == 0:  # Tile right
            dx = fk1
        elif di == 1:  # Tile up
            dx, dy = -fk2, fk1
        elif di == 2:  # Tile left
            dx, dy = -fk, -fk2
        elif di == 3:  # Tile down
            dy = -fk

        # Bottom-left corner of the k-th square
        x += dx
        y += dy

        # Update axes boundaries as needed
        xmin = min(x, xmin)
        ymin = min(y, ymin)
        xmax = max(x + fk, xmax)
        ymax = max(y + fk, ymax)

        # Add the new square to the list
        squares.append(Rectangle((x, y), fk, fk))

    # The collection of Patch objects representing squares
    rect_collection = PatchCollection(squares, edgecolor="black")  # Edge color must visually separate squares
    rect_collection.set(array=np.asarray(range(n + 1)), cmap="rainbow")  # Each square color from rainbow palette

    # Customize plot
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.add_collection(rect_collection)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal", "box")
    plt.tight_layout()
    plt.show()


plot_spiral(10)
