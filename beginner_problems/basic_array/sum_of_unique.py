==================================================================================================
# 4. Sum of Unique Elements
==================================================================================================
'''
You are given an integer array nums.
The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.

Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
'''
==================================================================================================
# Optimal Solution
==================================================================================================
# Using Counter builtin function

from collections import Counter
class Solution(object):
    def sumOfUnique(self, nums):
        s = Counter(nums)
        sum = 0
        for k, v in s.items():
            if v == 1:
                sum += k
        return sum
==================================================================================================
