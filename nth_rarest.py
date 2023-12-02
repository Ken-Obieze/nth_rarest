#!/usr/bin/python3
"""Module for defining nth_,ost_rare functions."""

def nth_most_rate(lst, n):
    """Check for the least occurence from a list."""
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    
    sorted_nums = sorted(freq.keys(), key=lambda x: freq[x])
    
    if n <= len(sorted_nums):
        return sorted_nums[n - 1]
    else:
        return None
