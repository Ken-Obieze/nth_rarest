# nth_most_rare Function

This Python function, `nth_most_rate`, identifies the nth rarest item in a list of integers based on their occurrence frequency.

## Cloning the Repository

To clone the `nth_rarest` repository, use the following command in your terminal:

```bash
git clone https://github.com/Ken-Obieze/nth_rarest.git
```

## Main Code

The function logic resides in the `nth_most_rare` function within the `nth_rarest.py` file. Here's the code:

```python
# nth_rarest.py

def nth_most_rate(lst, n):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    
    sorted_nums = sorted(freq.keys(), key=lambda x: freq[x])
    
    if n <= len(sorted_nums):
        return sorted_nums[n - 1]
    else:
        return None
```

The following codes tests the code with the given list  values to get the initial value of 2
```python
# main.py
#!/usr/bin/python3
"""
main
"""

from nth_rarest import nth_most_rate

nums = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
n_value = 2
result = nth_most_rate(nums, n_value)

if __name__ == "__main__":
    print(result)
```

# Test Code
The test_nth_rarest.py file contains test cases to validate the functionality of nth_most_rare. Here's the code:
```python
# test_nth_rarest.py

from nth_rarest import nth_most_rate

# Test cases
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
```
