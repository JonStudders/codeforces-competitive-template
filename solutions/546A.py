# ------------------------------
# Author: Jon Studders
# Created: 23/11/2025
# Problem: 546A
# ------------------------------

import sys
import math
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

# IO
input = sys.stdin.readline  # Faster input (reads directly from stdin)


def inp() -> int:
    """Reads a single integer."""
    return int(input())


def inlt() -> list[int]:
    """Reads a line of space-separated integers and returns them as a list."""
    return list(map(int, input().split()))


def invr():
    """Reads a line of space-separated integers and returns them as an iterator."""
    return map(int, input().split())


def insr() -> list[str]:
    """Reads a string and returns a list of its characters (excluding the newline)."""
    return list(input().strip())


def inps() -> str:
    """Reads a single line as a string (excluding the newline)."""
    return input().strip()


# Solution
def solve():
    k, n, w = inlt()
    first_banana_cost = k
    initial_balance = n
    total_bananas = w
    cost = 0
    for i in range(1, total_bananas + 1):
        # Purchase banana
        cost = cost + (i * first_banana_cost)

    if cost < initial_balance:
        print (0)
    else:
        print (cost - initial_balance)

if __name__ == "__main__":
    solve()
