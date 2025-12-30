=================================================================
# 242. Valid Anagram
=================================================================

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
=================================================================
# Brute Force
=================================================================
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        sort_s = sorted(s)
        sort_t = sorted(t)

        if sort_s == sort_t:
            return True
        return False      
"""
Step - 1:

- 2 str -> s, t
- anagram True or False

Step - 2:

- Input: s = "anagram", t = "nagaram" -> Sorted same values -> aaagmnr
  Output: true

- Input: s = "rat", t = "car"    -> art, acr wrong
  Output: false

- Same length strings

Step - 3:
Logic:
    - sort both values 
    - compare return value
"""
=================================================================
# Built - in
=================================================================
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
=================================================================
# Optimal Solution
=================================================================
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        mpp_s = {}
        mpp_t = {}    

        for i in s:
            if i in mpp_s:
                mpp_s[i] += 1
            else:
                mpp_s[i] = 1
        
        for i in t:
            if i in mpp_t:
                mpp_t[i] += 1
            else:
                mpp_t[i] = 1

        if mpp_s == mpp_t: # key & values must be same
            return True
        else:
            return False
=================================================================
        
