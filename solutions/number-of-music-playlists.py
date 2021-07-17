'''

Problem Statement: Number of Music Playlists

Link: https://leetcode.com/problems/number-of-music-playlists
Tags: ['Dynamic Programming']
Difficulty: Hard

Your music player contains n different songs and she wants to listen to goal (not necessarily different) songs during your trip.  You create a playlist so that:

Every song is played at least once
A song can only be played again only if k other songs have been played

Return the number of possible playlists.  As the answer can be very large, return it modulo 109 + 7.
 



Example 1:
Input: n = 3, goal = 3, k = 1
Output: 6
Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].


Example 2:
Input: n = 2, goal = 3, k = 0
Output: 6
Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]


Example 3:
Input: n = 2, goal = 3, k = 1
Output: 2
Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]



 
Note:

0 <= k < n <= goal <= 100






'''

