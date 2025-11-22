# ------------------------------
# Author: Jon Studders
# Created: 22/11/2025
# Problem: 617A
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
    x = inp()
    total = 0
    for i in range(5, 0, -1):
        steps = x // i
        dist = steps * i
        x = x - dist
        total = total + steps
    print (total)

if __name__ == "__main__":
    solve()
