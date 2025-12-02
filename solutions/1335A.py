# ------------------------------
# Author: Jon Studders
# Created: 22/11/2025
# Problem: 1335A
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
        a, b = inlt()
        if a == b:
            print(0)
        elif a % b == 0:
            print (0)
        else:
            c = True
            count = 0
            while c == True:
                if  a % b == 0:
                    c = False
                    print (count)
                else:
                    count = count + 1
                    a = a + 1
if __name__ == "__main__":
    solve()
