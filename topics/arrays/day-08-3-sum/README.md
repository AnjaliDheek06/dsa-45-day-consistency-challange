# Day 08 — 3 Sum (C++)

## Problem
Given an integer array `nums`, return all the triplets  
`[nums[i], nums[j], nums[k]]` such that:

- i != j
- i != k
- j != k
- nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.


## Approach

1️⃣ Sort the Array
The array is sorted first to:
- Use the two-pointer technique
- Easily handle duplicates

2️⃣ Fix One Element
Loop through the array using index `i`.

For each element:
- Treat `nums[i]` as the first element of the triplet.

3️⃣ Two Pointer Technique
- Set `left = i + 1`
- Set `right = n - 1`

While `left < right`:
- Calculate the sum
- If sum == 0 → store triplet
- If sum < 0 → move left pointer
- If sum > 0 → move right pointer

 4️⃣ Avoid Duplicates
- Skip duplicate values of `i`
- Skip duplicate values of `left`
- Skip duplicate values of `right`

This ensures unique triplets.


## Complexity Analysis

- Time Complexity: **O(n²)**
  - Outer loop runs n times
  - Inner two-pointer traversal takes O(n)

- Space Complexity: **O(1)** (excluding result storage)


## Key Learning

- Learned sorting + two pointer technique.
- Understood how to reduce brute force O(n³) to O(n²).
- Practiced duplicate handling carefully.
- Strengthened problem-solving for array-based interview questions.


## Pattern Used
Sorting + Two Pointer Technique