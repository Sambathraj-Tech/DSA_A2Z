=====================================================================================================
# 2. Factorial of a Given Number
=====================================================================================================
'''
Given an integer n, return the factorial of n.

Factorial of a non-negative integer,
is the multiplication of all integers smaller than or equal to n (use 64-bits to return answer).

Example 1
Input : n = 3
Output : 6
Explanation : Factorial = 1 * 2 * 3 => 6

Example 2
Input : n = 5
Output : 120Explanation : Factorial = 1 * 2 * 3 * 4 * 5 => 120

Example 3
Input : n = 4
Output: 24
'''
=====================================================================================================
# Solution
=====================================================================================================
class Solution:
    def factorial(self, n):
        #Your code goes here
        if n == 0:
            return 1
        return n * self.factorial(n - 1)
=====================================================================================================
