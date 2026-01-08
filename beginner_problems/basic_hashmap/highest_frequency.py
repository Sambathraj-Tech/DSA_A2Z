======================================================================================================
# 1. Highest Occurring Element in an Array
======================================================================================================
'''
Given an array nums of n integers, find the most frequent element in it i.e., 
the element that occurs the maximum number of times. 
If there are multiple elements that appear a maximum number of times, find the smallest of them.

Example 1
Input: nums = [1, 2, 2, 3, 3, 3]
Output: 3
Explanation: The number 3 appears the most (3 times). It is the most frequent element.

Example 2
Input: nums = [4, 4, 5, 5, 6]
Output: 4
Explanation: Both 4 and 5 appear twice, but 4 is smaller. So, 4 is the most frequent element.

Example 3
Input: nums = [2, 4, 3, 2, 5, 4]
Output:2
'''
======================================================================================================
# Optimal Approach
======================================================================================================
'''
Step - 1:  Understand the Question
array -> int
find  -> most occurences in the array

Step - 2: Explore Examples 
Input: nums = [1, 2, 2, 3, 3, 3]
Output: 3 

Step 3: Approach, Pattern Recognition 
1) Hashing
2) Empty dict then add nums as Keys
3) For every occurences add +1 Values in the dict
4) check which is largest number in the Values 
5) Return the largest Value of the KEY

Step 4: Time and Space complexity
Time  Complexity: O(N) 
Space Complexity: O(N)
'''
class Solution:
    def mostFrequentElement(self, nums):
        max_key = 0
        max_occ = 0
        mpp = {}

        for i in nums:
            if i in mpp:
                mpp[i] += 1
            else:
                mpp[i] = 1
        
        for k, v in mpp.items():
            if v > max_occ:
                max_occ = v
                max_key = k

            elif v == max_occ:
                max_key = min(max_key, k)

        return max_key
======================================================================================================
