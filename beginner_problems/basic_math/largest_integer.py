=================================================================
# 5. Return the Largest Digit in a Number
=================================================================

'''
You are given an integer n. Return the largest digit present in the number.

Example 1
Input: n = 25
Output: 5
Explanation: The largest digit in 25 is 5.

Example 2
Input: n = 99
Output: 9
Explanation: The largest digit in 99 is 9.
'''
=================================================================
# Optimal Solution
=================================================================
class Solution:
    def largestDigit(self, n):
        largest = 0
        while n > 0:
            last_digit = n % 10
            if last_digit > largest:
                largest = last_digit
            n = n // 10
        return largest
=================================================================
