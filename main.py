#!/usr/bin/python3
"""
0-main
"""

from nth_rarest import nth_most_rate

nums = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
n_value = 2
result = nth_most_rate(nums, n_value)

if __name__ == "__main__":
    print(result)
