"""
Title: Sliding Window Techniques

Description:
This Python code demonstrates various sliding window techniques, which are used to efficiently process subarrays
or subsequences of a fixed size within an array. Sliding window techniques are often applied to solve problems
like finding maximum subarray sums, moving averages, and more.

Usage:
1. Import or copy this code into your Python project.
2. Choose the specific sliding window technique (e.g., maximum subarray sum, moving averages) that suits your problem.
3. Implement the chosen technique using the provided functions and example code.

Example Usage (Maximum Subarray Sum):
arr = [1, 2, 3, 4, 5, 6, 7]
window_size = 3
max_sum = max_subarray_sum(arr, window_size)
print("Maximum Subarray Sum:", max_sum)  # Output: Maximum Subarray Sum: 18

"""

def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray of a fixed size k using the sliding window technique.

    Args:
    - arr (list): The input array.
    - k (int): The size of the sliding window.

    Returns:
    - int: The maximum subarray sum.
    """
    max_sum = current_sum = sum(arr[:k])

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

def moving_averages(arr, k):
    """
    Calculate the moving averages of a fixed-size window k using the sliding window technique.

    Args:
    - arr (list): The input array.
    - k (int): The size of the sliding window.

    Returns:
    - list: An array containing the moving averages.
    """
    averages = []
    current_sum = sum(arr[:k])

    for i in range(k, len(arr)):
        averages.append(current_sum / k)
        current_sum += arr[i] - arr[i - k]

    averages.append(current_sum / k)
    return averages

if __name__ == "__main__":
    import doctest

    doctest.testmod()
