====================================================================================================
# 3. Sum of Array Elements
====================================================================================================
'''
Given an array nums, find the sum of elements of array using recursion.

Example 1
Input : nums = [1, 2, 3]
Output : 6
Explanation : The sum of elements of array is 1 + 2 + 3 => 6.

Example 2
Input : nums = [5, 8, 1]
Output : 14
Explanation : The sum of elements of array is 5 + 8 + 1 => 14.

Example 3
Input : nums = [12, 9, 17]
Output: 38
'''
====================================================================================================
# Solution
====================================================================================================
class Solution:
    def arraySum(self, nums):
        #your code goes here
        return self.sumofarr(0, nums)
    
    def sumofarr(self, i, nums):
        if i >= len(nums):
            return 0
        
        return nums[i] + self.sumofarr(i + 1, nums)
====================================================================================================
====================================================================================================
