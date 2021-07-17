'''

Problem Statement: Broken Calculator

Link: https://leetcode.com/problems/broken-calculator
Tags: ['Math', 'Greedy']
Difficulty: Medium

On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.

Initially, the calculator is displaying the number x.
Return the minimum number of operations needed to display the number y.
 
Example 1:
Input: x = 2, y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

Example 2:
Input: x = 5, y = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.

Example 3:
Input: x = 3, y = 10
Output: 3
Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.

Example 4:
Input: x = 1024, y = 1
Output: 1023
Explanation: Use decrement operations 1023 times.

 
Note:

1 <= x <= 109
1 <= y <= 109



'''

