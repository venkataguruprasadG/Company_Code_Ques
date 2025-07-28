'''
Problem Statement:
Given an array of integers nums and an integer target, your task is to find two distinct indices i and j in the array such that the sum of the elements at these indices equals the target (i.e., nums[i] + nums[j] = target). You should return the indices as a list or tuple. Note that the same element cannot be used twice (i.e., i must not equal j), and you may assume there is exactly one valid solution.

Example:
Input: nums = [2, 7, 11,target = 9
Output: [0,
Explanation: nums + nums[1] = 2 + 7 = 9

Additional Details:

The order of the returned indices does not matter.

You only need to find one such pair that sums to the target.

The array may contain positive and/or negative integers.

What is being tested?

Array traversal

Ability to check pairs efficiently

Use of data structures like hash maps (dictionaries) for optimal lookup

Common Approaches:

Brute Force:
Check every pair (i, j) using nested loops to see if nums[i] + nums[j] == target. This has 
O(n2)time complexity.

Hash Map (Optimal):
Traverse the array once, and for each element nums[i], check if target - nums[i] has been seen before by storing elements in a hash map with their indices. This achieves 
O(n) time complexity.
'''

def Sum_of_two_numbers(nums,target):
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

