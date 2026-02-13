"""
Day 01 - Find the Largest Element in an Array

Problem Statement:
Given an array of integers, find the largest element.

Example:
Input: [4, 7, 3, 2, 6]
Output: 7

Approach:
- Initialize max_element with the first element
- Traverse the array
- Update max_element if current element is greater

Time Complexity: O(n)
Space Complexity: O(1)
"""


def get_largest(arr, n):
    max = arr[0]   #Accumulator pattern
    for i in range(1, n):
        if arr[i] > max:  
            max = arr[i]
    return max  

if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    n = len(arr1)  # Size of the array
    max = get_largest(arr1, n)  
    print("The largest element in the array is:", max)  

    