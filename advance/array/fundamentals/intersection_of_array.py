# Brute Force

from typing import List

class Solution:
    #Function to find intersection of two sorted arrays
    def intersectionArray(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans_list = []
        visited = [0] * len(nums2)
        i, j = 0, 0

        while i < len(nums1):
            while j < len(nums2):

                """ If nums1[i] is equal to nums2[j] and nums2[j] is
                    not visited then add nums2[j] in ans. """
                if nums1[i] == nums2[j] and visited[j] == 0:
                    
                    ans_list.append(nums2[j])
                    # Mark as visited
                    visited[j] = 1
                    
                    break
                 #If nums2[j] is greater than nums1[i], break out of loop
                elif nums2[j] > nums1[i]:
                    break
                j += 1
            i += 1
       
       #Return the final ans
        return ans_list

    def main(self):
        nums1 = [1, 2, 3, 3, 4, 5, 6, 7]
        nums2 = [3, 3, 4, 4, 5, 8]

        # Create an instance of the Solution class
        finder = Solution()

        # Get intersection of nums1 and nums2 using class method
        ans = finder.intersectionArrays(nums1, nums2)

        print("Intersection of nums1 and nums2 is:")
        print(ans)

if __name__ == "__main__":
    Solution().main()
  
---------------------------------------------------------------------------------------------
# Optimal Approach:

from typing import List

class Solution:
    #Function to find intersection of two sorted arrays
    def intersectionArray(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # List to store the intersection elements
        ans = []  

         # Pointers for nums1 and nums2
        i, j = 0, 0 

        # Traverse both arrays using two pointers approach
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
          # nums1[i] == nums2[j]
            else:  
                ans.append(nums1[i])
                i += 1
                j += 1

        return ans

    def main(self):
        # Array Initialization
        nums1 = [1, 2, 3, 3, 4, 5, 6, 7]
        nums2 = [3, 3, 4, 4, 5, 8]

        # Create an instance of the Solution class
        finder = Solution()

        """ Get intersection of nums1 
        and nums2 using class method"""
        ans = finder.intersectionArray(nums1, nums2)

        print("Intersection of nums1 and nums2 is:")

       #Print the intersection of two arrays
        print(ans)

# Execute main function
if __name__ == "__main__":
    Solution().main()

----------------------------------------------------------------------------------------------
