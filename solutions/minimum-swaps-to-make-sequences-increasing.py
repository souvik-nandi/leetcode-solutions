'''

Problem Statement: Minimum Swaps To Make Sequences Increasing

Link: https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing
Tags: ['Dynamic Programming']
Difficulty: Medium

We have two integer sequences nums1 and nums2 of the same non-zero length.
We are allowed to swap elements nums1[i] and nums2[i]. Note that both elements are in the same index position in their respective sequences.
At the end of some number of swaps, nums1 and nums2 are both strictly increasing. (An array A is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)
Given nums1 and nums2, return the minimum number of swaps to make both sequences strictly increasing. It is guaranteed that the given input always makes it possible.
Example:
Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
Output: 1
Explanation: 
Swap nums1[3] and nums2[3].  Then the sequences are:
nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
which are both strictly increasing.

Note:

nums1, nums2 are arrays with the same length, and that length will be in the range [1, 1000].
nums1[i], nums2[i] are integer values in the range [0, 2000].



'''

