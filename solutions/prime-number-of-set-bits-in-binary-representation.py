'''

Problem Statement: Prime Number of Set Bits in Binary Representation

Link: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation
Tags: ['Bit Manipulation']
Difficulty: Easy

Given two integers left and right, find the count of numbers in the range [left, right] (inclusive) having a prime number of set bits in their binary representation.
(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)
Example 1:
Input: left = 6, right = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)

Example 2:
Input: left = 10, right = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)

Note:

left, right will be integers left <= right in the range [1, 10^6].
right - left will be at most 10000.



'''

