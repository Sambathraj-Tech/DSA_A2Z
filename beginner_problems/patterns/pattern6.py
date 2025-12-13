class Solution:
    
    # Function to print pattern6
    def pattern6(self, n):
        
        # Outer loop will run for rows.
        for i in range(0,n):
            
            # Inner loop will run for columns.
            for j in range(0,n-i):
                print(j+1, end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern6(N)

if __name__ == "__main__":
    Solution().main()
