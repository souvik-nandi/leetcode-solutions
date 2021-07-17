'''

Problem Statement: Sum of Subsequence Widths

Link: https://leetcode.com/problems/sum-of-subsequence-widths
Tags: ['Array', 'Math']
Difficulty: Hard

Given an array of integers nums, consider all non-empty subsequences of nums.
For any sequence seq, let the width of seq be the difference between the maximum and minimum element of seq.
Return the sum of the widths of all subsequences of nums. 
As the answer may be very large, return the answer modulo 109 + 7.

 
Example 1:
Input: nums = [2,1,3]
Output: 6
Explanation:
Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.

 
Note:

1 <= nums.length <= 20000
1 <= nums[i] <= 20000




'''

