================================================================================================
# 5. Reverse an array
================================================================================================
'''
Given an array arr of n elements. The task is to reverse the given array.
The reversal of array should be inplace.

Example 1
Input: n=5, arr = [1,2,3,4,5]
Output: [5,4,3,2,1]
Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

Example 2
Input: n=6, arr = [1,2,1,1,5,1]
Output: [1,5,1,1,2,1]
Explanation: The reverse of the array [1,2,1,1,5,1] is [1,5,1,1,2,1].

Example 3
Input: n=3, arr = [1,2,1]
Output: [1,2,1]
'''
================================================================================================
# Optimal Approach (Two Pointer)
================================================================================================
class Solution:
    def reverse(self, arr: list, n: int) -> None:
        left = 0
        right = n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
================================================================================================
