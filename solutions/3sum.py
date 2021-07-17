'''

Problem Statement: 3Sum

Link: https://leetcode.com/problems/3sum
Tags: ['Array', 'Two Pointers']
Difficulty: Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
 
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:
Input: nums = []
Output: []
Example 3:
Input: nums = [0]
Output: []

 
Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

'''

'''
Solution:

Algorithm:
    1) Sort the list (will be required for 2 pointer search and removing duplicated)
    2) Iterate over each item to fix 'i'
    3) Run a 2 pointer loop one starting from i + 1 and another from n - 1 until j < k
        j -> i+1
        k -> n-1

    4) if sum(vals(i, j, k)) == 0, then increment j
    5) elif sum(vals(i, j, k)) < 0, then increment j
    6) else sum(vals(i, j, k)) > 0, then decrement k
    

Till this much it will provide all possible triplets with sum = 0, but there will be  duplicates 

Inorder to remove the duplicates same value should not appear for i and j
So we will add two more checks
    2.1) if val(i) == val(i-1) continue
    4.1) if j < k and val(j) == val(j-1) keep incrementing j
'''


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        if n < 3:
            return []
        
        triplets = []
        nums = sorted(nums)
        
        for i in range(n-2):
            # Never let i refer to the same value twice to avoid duplicates.
            if (i != 0 and nums[i] == nums[i - 1]): continue;
            i_val = nums[i]
            j = i + 1
            k = n - 1
            
            # Two pointer search starts
            while j < k:
                j_val = nums[j]
                k_val = nums[k]
                
                tot = i_val + j_val + k_val
                
                if tot == 0:
                    triplets.append([i_val, j_val, k_val])
                    j += 1
                    # Never let j refer to the same value twice (in an output) to avoid duplicates.
                    while (j < k and nums[j] == nums[j-1]): j += 1;
                elif tot < 0:
                    j += 1
                else:
                    k -= 1
        
        return triplets
            
                    