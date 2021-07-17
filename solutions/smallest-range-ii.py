'''

Problem Statement: Smallest Range II

Link: https://leetcode.com/problems/smallest-range-ii
Tags: ['Math', 'Greedy']
Difficulty: Medium

Given an array nums of integers, for each integer nums[i] we need to choose either x = -k or x = k, and add x to nums[i] (only once).
After this process, we have some array result.
Return the smallest possible difference between the maximum value of result and the minimum value of result.
 



Example 1:
Input: nums = [1], k = 0
Output: 0
Explanation: result = [1]


Example 2:
Input: nums = [0,10], k = 2
Output: 6
Explanation: result = [2,8]


Example 3:
Input: nums = [1,3,6], k = 3
Output: 3
Explanation: result = [4,6,3]

 
Note:

1 <= nums.length <= 10000
0 <= nums[i] <= 10000
0 <= k <= 10000






'''

