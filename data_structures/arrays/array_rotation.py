"""
Title: Array Rotation using Reversal Algorithm

Description:
This Python code demonstrates how to rotate an array to the right by a specified number of positions
using the Reversal Algorithm. Array rotation is a common problem, and this algorithm provides an
efficient solution with a time complexity of O(n), where n is the length of the array.

Usage:
1. Import or copy this code into your Python project.
2. Call the `rotate_array` function with your array and the number of positions to rotate.
3. The rotated array will be modified in place.

Example Usage:
arr = [1, 2, 3, 4, 5, 6, 7]
rotate_array(arr, 3)
print(arr)  # Output: [5, 6, 7, 1, 2, 3, 4]

"""

def reverse(arr, start, end):
    """
    Reverse a subarray within the given range.

    Args:
    - arr (list): The input array.
    - start (int): The start index of the subarray to reverse.
    - end (int): The end index of the subarray to reverse.
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, d):
    """
    Rotate an array to the right by a specified number of positions using the Reversal Algorithm.

    Args:
    - arr (list): The input array to be rotated.
    - d (int): The number of positions to rotate the array to the right.
    """
    n = len(arr)
    d = d % n  # Handle cases where d is greater than the array length
    reverse(arr, 0, n - 1)  # Reverse the entire array
    reverse(arr, 0, d - 1)  # Reverse the first part of the array (0 to d-1)
    reverse(arr, d, n - 1)  # Reverse the second part of the array (d to n-1)
    
if __name__ == "__main__":
    import doctest

    doctest.testmod()
