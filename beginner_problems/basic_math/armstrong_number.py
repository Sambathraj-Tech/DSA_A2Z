=====================================================================================================
# 7. Check for Armstrong Number
=====================================================================================================
'''
You are given an integer n. You need to check whether it is an armstrong number or not.
Return true if it is an armstrong number, otherwise return false.
An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

Example 1
Input: n = 153
Output: true
Explanation: Number of digits : 3.
13 + 53 + 33 = 1 + 125 + 27 = 153.
Therefore, it is an Armstrong number.

Example 2
Input: n = 12
Output: false
Explanation: Number of digits : 2.
12 + 22 = 1 + 4 = 5.
Therefore, it is not an Armstrong number.
'''
=====================================================================================================
class Solution:
    def isArmstrong(self, n):
        length = len(str(n))
        result = n
        armstrong = 0
        while n > 0:
            last_digit = n % 10
            armstrong = (armstrong) + (last_digit ** length)
            n = n // 10
        return armstrong == result
=====================================================================================================
