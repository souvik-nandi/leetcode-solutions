'''

Problem Statement: Maximum Sum Circular Subarray

Link: https://leetcode.com/problems/maximum-sum-circular-subarray
Tags: ['Array']
Difficulty: Medium

Given a circular array circ of integers represented by nums, find the maximum possible sum of a non-empty subarray of circ.
Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, circ[i] = nums[i] when 0 <= i < nums.length, and circ[i+nums.length] = circ[i] when i >= 0.)
Also, a subarray may only include each element of the fixed buffer nums at most once.  (Formally, for a subarray circ[i], circ[i+1], ..., circ[j], there does not exist i <= k1, k2 <= j with k1 % nums.length = k2 % nums.length.)
 

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3


Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10


Example 3:
Input: nums = [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4


Example 4:
Input: nums = [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:
Input: nums = [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

 
Note: 

-30000 <= nums[i] <= 30000
1 <= nums.length <= 30000







'''

