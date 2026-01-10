=====================================================================================================
# 4. Reverse the String
=====================================================================================================
'''
Given an input string as an array of characters, write a function that reverses the string.

Example 1
Input : s = ["h", "e", "l", "l", "o"]
Output : ["o", "l", "l", "e", "h"]
Explanation : The given string is s = "hello" and after reversing it becomes s = "olleh".

Example 2
Input : s = ["b", "y", "e" ]
Output : ["e", "y", "b"]
Explanation : The given string is s = "bye" and after reversing it becomes s = "eyb".
'''
=====================================================================================================
# Solution
=====================================================================================================
class Solution:
    def reverseString(self,s):
        #your code goes here
        return self.reverse(0, len(s) - 1, s)

    def reverse(self, l, r, s):
        if l >= r:
            return s
        
        s[l], s[r] = s[r], s[l]
        return self.reverse(l + 1, r - 1, s)
=====================================================================================================
