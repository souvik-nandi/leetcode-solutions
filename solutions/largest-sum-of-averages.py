'''

Problem Statement: Largest Sum of Averages

Link: https://leetcode.com/problems/largest-sum-of-averages
Tags: ['Dynamic Programming']
Difficulty: Medium

We partition a row of numbers nums into at most k adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?
Note that our partition must use every number in nums, and that scores are not necessarily integers.
Example:
Input: 
nums = [9,1,2,3,9]
k = 3
Output: 20
Explanation: 
The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

 
Note: 

1 <= nums.length <= 100.
1 <= nums[i] <= 10000.
1 <= k <= nums.length.
Answers within 10-6 of the correct answer will be accepted as correct.



'''

