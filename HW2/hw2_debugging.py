"""
This module implements the merge sort algorithm for sorting arrays.

It defines two main functions:
- merge_sort: Recursively divides and sorts an array.
- recombine: Merges two sorted arrays into one sorted array.
"""

import rand

def merge_sort(input_array):
    """
    Recursively sorts an array using the merge sort algorithm.

    """
    if len(input_array) <= 1:
        return input_array

    half = len(input_array) // 2
    left_sorted = merge_sort(input_array[:half])
    right_sorted = merge_sort(input_array[half:])

    return recombine(left_sorted, right_sorted)


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into one sorted array.

    """
    left_index = 0
    right_index = 0
    merge_arr = []

    # Merge the elements from both arrays in sorted order
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    # Add remaining elements from left_arr
    while left_index < len(left_arr):
        merge_arr.append(left_arr[left_index])
        left_index += 1

    # Add remaining elements from right_arr
    while right_index < len(right_arr):
        merge_arr.append(right_arr[right_index])
        right_index += 1

    return merge_arr

# Generate a random array
arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)
print(arr_out)
