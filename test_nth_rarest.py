#!/usr/bin/python3
"""module for testing nth_most_rare function"""
from nth_rarest import nth_most_rate

def test_case_1():
    nums = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
    n_value = 2
    assert nth_most_rate(nums, n_value) == 2

def test_case_2():
    nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    n_value = 1
    assert nth_most_rate(nums, n_value) == 3

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    print("All tests passed successfully!")
