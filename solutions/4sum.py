'''

Problem Statement: 4Sum

Link: https://leetcode.com/problems/4sum
Tags: ['Array', 'Hash Table', 'Two Pointers']
Difficulty: Medium

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
 
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

 
Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109



'''

'''
Solution:

This solution expects non-repeating indexes.
Check 3sum.py for the algorithm
'''


from typing import List


class Solution1:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        
        if n < 3:
            return []
        
        triplets = []
        
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
                
                if tot == target:
                    triplets.append([i_val, j_val, k_val])
                    j += 1
                    # Never let j refer to the same value twice (in an output) to avoid duplicates.
                    while (j < k and nums[j] == nums[j-1]): j += 1;
                elif tot < target:
                    j += 1
                else:
                    k -= 1
        
        return triplets
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        
        if n < 4:
            return []
        
        quadruplets = []
        nums = sorted(nums)
        
        for i in range(n-3):
            # Never let i refer to the same value twice to avoid duplicates.
            if (i != 0 and nums[i] == nums[i - 1]): continue;
            triplets = self.threeSum(nums[i+1:], target - nums[i])

            if bool(triplets):
                for comb in triplets:
                    quadruplets.append([nums[i]] + comb)
                
        return quadruplets



'''
Faster recursive solution for variable size of combination
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1
            while (lo < hi):
                sum = nums[lo] + nums[hi]
                if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
