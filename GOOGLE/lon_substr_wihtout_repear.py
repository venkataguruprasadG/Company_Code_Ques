'''
Problem Statement:
Given a string s, find the length of the longest substring without any repeating characters. A substring is a contiguous sequence of characters within the string. Your task is to identify such a substring where all characters are unique and determine its length.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The longest substring without repeating characters is "abc", with a length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The longest substring without repeating characters is "b", with a length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The longest substring is "wke", with a length of 3. Note that "pwke" is not a valid answer because characters must be contiguous.

Clarifications and Constraints:

You must return the length of the longest substring, not the substring itself.

The input string can contain any ASCII characters, including letters, digits, and symbols.

The string may be empty; in that case, the answer is 0.

What is being tested?

Your ability to process substrings and handle repeated elements efficiently.

Understanding and implementing the sliding window technique.

Efficient use of data structures such as sets or hash maps.

Common Approaches:

Brute Force: Try all possible substrings, check each for uniqueness—has O(n³) time complexity.

Sliding Window:

Use two pointers to define a window in the string.

Expand the end pointer to include new characters; shrink the start pointer when a duplicate is encountered.

Keep a set or hash map to track characters in the current window.

This approach yields O(n) time complexity
'''

class Solution:
    def lengthofthesubstring(self, s:str) -> int:
        max_length=0
        for i in range(len(s)):
            seen = set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_length=max(max_length,j-i+1)
