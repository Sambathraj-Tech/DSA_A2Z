You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) 
that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
  
============================================================================================
Brute Force:

class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        s = int(num)
        while s > 0:
            last_digit = s % 10 
            if last_digit % 2 == 1:
                return str(s)
            s = s // 10
        return ""

"""
Step -1 :

- string -> num
- return -> str (largest odd number)
- "" -> empty str not allowed

Step -2 :

- Input : "52" , "4206"
- Output: "5" ,  ""       # when even number is only there return ""

Step - 3:

logic: i will see from last integer which is odd or not (if not return "")
        if odd i will take all the before values as largest 
        
"""
=================================================================================
Optimal Approach:

class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        i = len(num) - 1
        while i >= 0:
            if num[i] in "13579":
                return num[:i + 1]
            i -= 1
        return ""
