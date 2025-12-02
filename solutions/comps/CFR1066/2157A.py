# ------------------------------
# Author: Jon Studders
# Created: 23/11/2025
# Problem: 2157A
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
        a = inlt()
        a.sort()
        result = []
        count = 0
        for i in range(n):
            x = a.count(a[i])
            if x == a[i]:
                if a[i] not in result:
                    result.append(a[i])
            elif x > a[i]:
                if a[i] not in result:
                    o = x - a[i]
                    count = count + o
                    result.append(a[i])
            else:
                if a[i] not in result:
                    count = count + x
                    result.append(a[i])
        print(count)

if __name__ == "__main__":
    solve()
