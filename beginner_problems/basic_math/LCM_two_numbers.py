============================================================================================
# 12. LCM of two numbers
============================================================================================
'''
You are given two integers n1 and n2. You need find the Lowest Common Multiple (LCM) of the two given numbers.
Return the LCM of the two numbers.
The Lowest Common Multiple (LCM) of two integers is the lowest positive integer that is divisible by both the integers.

Example 1
Input: n1 = 4, n2 = 6
Output: 12
Explanation: 4 * 3 = 12, 6 * 2 = 12.
12 is the lowest integer that is divisible both 4 and 6.

Example 2
Input: n1 = 3, n2 = 5
Output: 15
Explanation: 3 * 5 = 15, 5 * 3 = 15.
15 is the lowest integer that is divisible both 3 and 5.

Example 3
Input: n1 = 4, n2 = 12
Output: 12
'''
============================================================================================
# Brute Force
============================================================================================
# Using for loop

class Solution:
    def LCM(self, n1, n2):
        lcm = 0
        n = max(n1, n2)
        
        for i in range(1, max(n1, n2), 1):
            mult = n * i
            if mult % n1 == 0 and mult % n2 == 0:
                lcm = mult
                break
            
        return lcm
============================================================================================
# Optimal Approach
============================================================================================
class Solution:
  
# Eucleadian Formula 
  
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
        
    def LCM(self, n1, n2):

        gcd = self.GCD(n1, n2)
        lcm = (n1 * n2) // (gcd)
        return lcm
============================================================================================
