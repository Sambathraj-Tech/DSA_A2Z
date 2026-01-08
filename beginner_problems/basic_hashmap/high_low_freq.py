=================================================================================================
# 3. Highest and Lowest Sum of Frequency
=================================================================================================
'''
Given an array of n integers, 
find the sum of the frequencies of the highest occurring number and lowest occurring number.

Example 1

Input: arr = [1, 2, 2, 3, 3, 3]
Output: 4
Explanation: The highest frequency is 3 (element 3), and the lowest frequency is 1 (element 1). Their sum is 3 + 1 = 4.

Example 2
Input: arr = [4, 4, 5, 5, 6]
Output: 3
Explanation: The highest frequency is 2 (elements 4 and 5), and the lowest frequency is 1 (element 6). Their sum is 2 + 1 = 3.

Example 3
Input: arr = [10, 9, 7, 7, 8, 8, 8]
Output: 4
'''
=================================================================================================
# First Approach
=================================================================================================
class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        mpp = {}
        for i in nums:
            if i in mpp:
                mpp[i] += 1
            else:
                mpp[i] = 1
        
        max_val = max(mpp.values())
        min_val = min(mpp.values())
        total = max_val + min_val
        return total
=================================================================================================
