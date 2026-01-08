========================================================================================================================
# 13. Add Digits
========================================================================================================================
'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
              38 --> 3 + 8 --> 11
              11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0
'''
========================================================================================================================
# Optimal Solution (Math Logic)
========================================================================================================================
'''
Approach:

Base Case Check:
If the input number num is 0, the result is 0 because the digital root of 0 is 0.

Divisibility Check:
If num is divisible by 9, return 9. 
This is because any number that is a multiple of 9 has a digital root of 9 (except for 0).

General Case:
For all other numbers, return num % 9. This remainder gives the digital root directly. 
This is based on the properties of numbers and modulo arithmetic, 
which simplifies the process to a constant-time solution.
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: 
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
========================================================================================================================
# Time Complexity : O(1)
# Space Complexity : O(1)
========================================================================================================================
