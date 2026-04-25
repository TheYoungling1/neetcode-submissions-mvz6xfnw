class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force, o(n^3)

        # find all substring combinations, for each substring, 
        # cycle to the end to check if its a palindrome

        # 2d dp approach where cols and rows represent the i and j bounds of a
        # substring, so realistically, only half of this matrix would be filled
        # as substring 1 - 3 = 3 - 1
    
        # how can we break this problem down

        #  what about if for each field in the dp matrix
        # each cell is te string from i (row) num to j (col) num

        # so [1][3] = substring reading from 1 to 3
        # and [3][1] = substring reading from 3 to 1

        # if [1][3] == [3][1] return true?

        # how does a palindrome relate to recursion
        # abba 
        # 2 recursive calls from opposite ends should have the same output
        # thats how to know if its a recursion

        ROWS = len(s)
        COLS = len(s)

        dp = []
        for i in range(ROWS):
            # 1. Create a brand new row for every 'i'
            row = []
            for j in range(COLS):
                # 2. Fill that row with the initial value
                row.append(-1)
            # 3. Add the completed row to your main list
            dp.append(row)
        

        def palindrome(i, j):    
            if i >= len(s) or j < 0 or s[i] != s[j]:
                return False
            
            if i == j or (i + 1) == j:
                return True
            
            # can have substring in between

            if dp[i+1][j-1] != -1:
                return s[i] == s[j] and dp[i + 1][j - 1]
            
            if s[i] == s[j]:
                dp[i][j] = palindrome(i + 1, j - 1)
            else:
                dp[i][j] = False

            return dp[i][j]

        max_str = ""
        for i in range(ROWS):
            for j in range(i, COLS):
                if palindrome(i, j):
                    if (j - i + 1) > len(max_str):
                        max_str = s[i:j+1]
        return max_str

        # cycle through the matrix to file the largest cell whose j - i 
        # is true






