==============================================================================================
# 3. Count of Odd numbers in the array
==============================================================================================
'''
Given an array of n elements. 
The task is to return the count of the number of odd numbers in the array.

Example 1
Input: n=5, array = [1,2,3,4,5]
Output: 3
Explanation: The three odd elements are (1,3,5).

Example 2
Input: n=6, array = [1,2,1,1,5,1]
Output: 5
Explanation: The five odd elements are one 5 and four 1's.

Example 3
Input: n=5, array = [1,3,5,7,9]
Output: 5
'''
==============================================================================================
# Solution
==============================================================================================
class Solution:
    def countOdd(self, arr, n):
        # Your code goes here
        count = 0
        for i in range(0, n, 1):
            if arr[i] % 2 == 1:
                count += 1
        return count
==============================================================================================
