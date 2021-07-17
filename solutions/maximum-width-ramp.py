'''

Problem Statement: Maximum Width Ramp

Link: https://leetcode.com/problems/maximum-width-ramp
Tags: ['Array']
Difficulty: Medium

Given an array nums of integers, a ramp is a tuple (i, j) for which i < j and nums[i] <= nums[j].  The width of such a ramp is j - i.
Find the maximum width of a ramp in nums.  If one doesn't exist, return 0.
 
Example 1:
Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: 
The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.


Example 2:
Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: 
The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.




 
Note:

2 <= nums.length <= 50000
0 <= nums[i] <= 50000




 



'''

