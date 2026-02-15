# Day 03 — Count Frequency in Array

## Problem
Given an array, we have found the number of occurrences of each element in the array.

## Approach
Used a hash map (defaultdict) to store frequency of elements.
Traverse the array once.
For each element, increment its count in the dictionary.
Finally, iterate over the dictionary to print each element and its frequency.
This ensures counting happens in a single pass.

## Complexity
 Time: O(n)  since only one traversal
Space: O(n) for storing frequencies of unique elements in the unordered_map.

## Key Learning
Learned how to use hash maps (dictionary) for frequency counting.
Understood how defaultdict(int) automatically initializes missing keys.
Practiced linear traversal combined with dynamic counting.
Recognized this as a common interview pattern (frequency counting).