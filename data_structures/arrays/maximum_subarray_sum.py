"""
Title: Kadane's Algorithm for Maximum Subarray Sum

Description:
Kadane's Algorithm is used to find the maximum subarray sum in a given array of integers. This algorithm efficiently handles both positive and negative numbers and has a time complexity of O(n), where n is the length of the array.

Usage:
1. Import or copy this code into your Python project.
2. Call the `kadanes_algorithm` function with your array.
3. The function will return the maximum subarray sum.

Example Usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = kadanes_algorithm(arr)
print("Maximum Subarray Sum:", max_sum)  # Output: Maximum Subarray Sum: 6

"""

def kadanes_algorithm(arr):
    """
    Find the maximum subarray sum using Kadane's Algorithm.

    Args:
    - arr (list): The input array of integers.

    Returns:
    - int: The maximum subarray sum.
    """
    max_ending_here = max_so_far = arr[0]

    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


if __name__ == "__main__":
    import doctest

    doctest.testmod()
