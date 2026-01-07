==============================================================================
# 13. Divisor of a number
==============================================================================
'''
You are given an integer n. You need to find all the divisors of n.
Return all the divisors of n as an array or list in a sorted order.
A number which completely divides another number is called it's divisor.

Example 1

Input: n = 6
Output = [1, 2, 3, 6]
Explanation: The divisors of 6 are 1, 2, 3, 6.

Example 2
Input: n = 8
Output: [1, 2, 4, 8]
Explanation: The divisors of 8 are 1, 2, 4, 8.

Example 3
Input: n = 7
Output: [1, 7]
'''
==============================================================================
# Optimal Soltion
==============================================================================
import math
class Solution:
    def divisors(self, n):
        if n < 1:
            return False
        result = []
        for i in range(1, int(math.sqrt(n)) + 1, 1):
            if n % i == 0:
                result.append(i)
                if i * i != n:
                    result.append(n // i)
        
        result.sort()
        return result
==============================================================================
