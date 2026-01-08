===============================================================================================
# 2. Second Highest Frequency
===============================================================================================
'''
Given an array of n integers, find the second most frequent element in it.
If there are multiple elements that appear second most frequent times, find the smallest of them.
If second most frequent element does not exist return -1.

Example 1
Input: arr = [1, 2, 2, 3, 3, 3]
Output: 2
Explanation: The number 2 appears the second most (2 times) and number 3 appears the most(3 times). 

Example 2
Input: arr = [4, 4, 5, 5, 6, 7]
Output: 6
Explanation: Both 6 and 7 appear second most times, but 6 is smaller.

Example 3

Input: arr = [10, 9 ,7, 7]
Output: 9
'''
===============================================================================================
# Optimal Solution
===============================================================================================
'''
Step - 1:  Understand the Question
array -> int
find  -> most occurences in the array

Step - 2: Explore Examples 
Input: nums = [1, 2, 2, 3, 3, 3]
Output: 2

Input: arr = [4, 4, 5, 5, 6, 7]
Output: 6 --> 6 is smaller.

Step 3: Approach, Pattern Recognition 
1) Hashing
2) Empty dict then add nums as Keys
3) Four variables -> max_key, value & sec_max_key, value
4) check the array if the [num] in the empty_dict (add +1)
5) else: initiate 1 in the value
6) After all that check max_val > [v] in the dict
7) If greater then  max_val = v & sec_max_val = max_val
8) At the same time max_key = k & sec_max_key = max_key
9) If max_val and v is equal take the [min] KEY
10) If sec_max_val and v is equal take the [min] KEY

Step 4: Time and Space complexity
Time  Complexity: O(N) 
Space Complexity: O(N)
'''
from collections import defaultdict
class Solution:
    def secondMostFrequentElement(self, nums):
        max_key = -1
        max_val = 0
        sec_max_key = -1
        sec_max_val = 0
        mpp = defaultdict(int)

        for i in nums:
            mpp[i] += 1
            
        for k, v in mpp.items():
            if v > max_val:
                sec_max_val = max_val
                max_val = v
                sec_max_key = max_key
                max_key = k
            
            elif v == max_val:
                max_key = min(max_key, k)
            
            elif v > sec_max_val:
                sec_max_val = v
                sec_max_key = k

            elif v == sec_max_val:
                sec_max_key = min(sec_max_key, k)
            
        return sec_max_key
===============================================================================================
