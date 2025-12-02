# ------------------------------
# Author: Jon Studders
# Created: 28/11/2025
# Problem: 2170A
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
    t = inp()
    for _ in range(t):
        n = inp()
        if n == 1:
            print (1)
        elif n == 2:
            print (9)
        elif n == 3 or n == 4:
            right = n*n
            mid = right - 1
            left = mid - 1
            above = mid - n
            print (right+mid+left+above)
        else:
            mid = ((n*n) - (n+1))
            above = mid - n
            below = mid + n
            left = mid - 1
            right = mid + 1
            print (mid+above+below+left+right)


if __name__ == "__main__":
    solve()
