class Solution:
    
    # Function to print pattern1
    def pattern1(self, n):
        
        # Outer loop will run for rows.
        for i in range(n):
            
            # Inner loop will run for columns.
            for j in range(n):
                print("*", end="")
                
            """ As soon as N stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 4

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern1(N)

if __name__ == "__main__":
    Solution().main()
