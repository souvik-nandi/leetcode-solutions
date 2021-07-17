'''

Problem Statement: Split Array into Consecutive Subsequences

Link: https://leetcode.com/problems/split-array-into-consecutive-subsequences
Tags: ['Heap', 'Greedy']
Difficulty: Medium

Given an integer array nums that is sorted in ascending order, return true if and only if you can split it into one or more subsequences such that each subsequence consists of consecutive integers and has a length of at least 3.
 
Example 1:
Input: nums = [1,2,3,3,4,5]
Output: true
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:
Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:
Input: nums = [1,2,3,4,4,5]
Output: false

 
Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
nums is sorted in an ascending order.



'''

