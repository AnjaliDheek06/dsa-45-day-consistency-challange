# Day 09 — Sum of Series

## Problem

Given an integer n. Your task is to calculate the sum of all natural numbers from 1 up to n (inclusive). If n is 0, the sum should be 0.

## Approach (Using Mathematical Formula)

Use the mathematical formula:

Sum = n × (n + 1) / 2

If n is 0, return 0.
This avoids using loops and directly calculates the result in constant time.

## Complexity

Time Complexity  :   Using formula → O(1)

Space Complexity :  No extra space used → O(1)

## Key Learning

Used mathematical formula to eliminate iteration.
Optimized from O(n) loop approach to O(1) constant time solution.
Learned how to prevent overflow using long long for large inputs.
Understood difference between iterative and formula-based optimization.

