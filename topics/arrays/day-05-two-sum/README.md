# Day 05 — Leetcode two sum problem 

## Problem
Given two integer arrays nums1 and nums2, return the union of both arrays.
The union of two arrays contains all unique elements from both arrays.
You can return the result in any order.

## Approach(using set)
Convert both arrays into a set.
Use the union() operation or | operator.
Convert the result back to a list.

## Complexity
Time Complexity:  Converting both arrays into sets → O(n + m) , Union operation → O(n + m) ,  Overall: O(n + m) where n is length of nums1  and m = length of nums2

Space Complexity: We store unique elements in a set → O(n + m)

## Key Learning
Used HashMap (Dictionary) for constant-time lookups → O(1) average access.
Optimized brute-force O(n²) approach to O(n) time complexity.
Avoided using the same element twice by checking before inserting into hashmap.


