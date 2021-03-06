'''

Problem Statement: Random Pick with Blacklist

Link: https://leetcode.com/problems/random-pick-with-blacklist
Tags: ['Hash Table', 'Binary Search', 'Sort', 'Random']
Difficulty: Hard

Given a blacklist blacklist containing unique integers from [0, n), write a function to return a uniform random integer from [0, n) which is NOT in blacklist.
Optimize it such that it minimizes the call to system’s Math.random().
Note:

1 <= n <= 1000000000
0 <= blacklist.length < min(100000, n)
[0, n) does NOT include n. See interval notation.

Example 1:
Input: 
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]

Example 2:
Input: 
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]

Example 3:
Input: 
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]

Example 4:
Input: 
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]

Explanation of Input Syntax:
The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, n and the blacklist blacklist. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.


'''

