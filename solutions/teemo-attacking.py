'''

Problem Statement: Teemo Attacking

Link: https://leetcode.com/problems/teemo-attacking
Tags: ['Array']
Difficulty: Medium

You are given an integer array timeSeries and an integer duration. Our hero Teemo has attacked an enemy where the ith attack was done at the timeSeries[i]. When Teemo attacks their enemy, the enemy gets poisoned for duration time (i.e., the enemy is poisoned for the time interval [timeSeries[i], timeSeries[i] + duration - 1] inclusive).
Return the total time that the enemy is in a poisoned condition.
 
Example 1:
Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: At time point 1, Teemo starts attacking the enemy and makes them be poisoned immediately. 
This poisoned status will last 2 seconds until the end of time point 2. 
And at time point 4, Teemo attacks the enemy again and causes them to be in poisoned status for another 2 seconds. 
So you finally need to output 4.

Example 2:
Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: At time point 1, Teemo starts attacking the enemy and makes them be poisoned. 
This poisoned status will last 2 seconds until the end of time point 2. 
However, at the beginning of time point 2, Teemo attacks the enemy again who is already in poisoned status. 
Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. 
So you finally need to output 3.

 
Constraints:

1 <= timeSeries.length <= 104
0 <= timeSeries[i], duration <= 107
timeSeries is sorted in non-decreasing order.



'''

