===========================================================================
# 11. GCD of tow numbers
===========================================================================
'''
You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers.
Return the GCD of the two numbers.
The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.

Example 1
Input: n1 = 4, n2 = 6
Output: 2
Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6
Greatest Common divisor = 2.

Example 2
Input: n1 = 9, n2 = 8
Output: 1
Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.
Greatest Common divisor = 1.

Example 3
Input: n1 = 6, n2 = 12
Output: 6
'''
===========================================================================
# Brute Force
===========================================================================
class Solution:
    def GCD(self, n1, n2):
        # we know 1 is the common divisor for all numbers
        largest = 1
        for i in range(2, min(n1, n2), 1):
            if n1 % i == 0 and n2 % i == 0:
                largest = i
        
        return largest
===========================================================================
# Better Solution
===========================================================================
class Solution:
    def GCD(self, n1, n2):

        for i in range(min(n1, n2), 0,  -1):
            if n1 % i == 0 and n2 % i == 0:
                return i

# Just change the loop direction and return the highest
===========================================================================
# Optimal Approach
===========================================================================
class Solution:
    def GCD(self, n1, n2):
        gcd = 0
        while n1 != 0 and n2 != 0:
            if n1 > n2:
                n1 = n1 % n2
            else:
                n2 = n2 % n1
            
            if n1 == 0:
                gcd = n2
            else:
                gcd = n1
        
        return gcd
===========================================================================
