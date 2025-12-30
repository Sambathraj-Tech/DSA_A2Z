=================================================================
# 796. Rotate String
=================================================================
'''
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
 
Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false
'''
=================================================================
# Brute Force
=================================================================
class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        for i in range(0, len(s)):
            res = s[i:] + s[:i]
            if res == goal:
                return True
        return False
      
"""
Step - 1:
- 2 str -> s , goal
- return True  s  can become goal after number of shifts
- shifting is happen by leftmost - rightmost position
- eg : s = "abcde" -> "bcdea" after one shift.

Step - 2:
- Input: s = "abcde", goal = "cdeab"
- Output: true
- Input: s = "abcde", goal = "abced"
- Output: false

- Only can rotate not interchange 

Step - 3:
Logic:
    - String slicing 
    - Check it True or not 
"""
=================================================================
# Optimal Solution
=================================================================
class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        c = s+s
        return goal in c
=================================================================
        
