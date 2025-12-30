=================================================================
# 205. Isomorphic Strings
=================================================================

'''Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Explanation: The strings s and t can be made identical by: 
  Mapping 'e' to 'a'.
  Mapping 'g' to 'd'.

Example 2:

Input: s = "foo", t = "bar"
Output: false
Explanation: The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"
Output: true
'''
=================================================================
# Brute Force
=================================================================
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        d1 = [0] * 256
        d2 = [0] * 256

        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            
            d1[ord(s[i])] = i + 1
            d2[ord(t[i])] = i + 1
        
        return True
   
"""
Step - 1:

2 strings -> s, t and find isomorphic
char only map to same character

Step - 2:

Input: s = "egg", t = "add"
    e -> a
    g -> d
    g -> d
output : True

Input: s = "foo", t = "bar"
    f -> b
    o -> a
    o -> r
output : fasle

Step - 3:

take 256 [0] as d1, d2
compare the index of both d1, d2
if same add i + 1
else return False
"""
=================================================================
# Optimal Solution
=================================================================
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        d1 = {}
        d2 = {}

        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = i
            if t[i] not in d2:
                d2[t[i]] = i
            if d1[s[i]] != d2[t[i]]:
                return False
        return True
=================================================================
        
