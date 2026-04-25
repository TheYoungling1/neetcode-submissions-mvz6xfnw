class Solution:
    def countSubstrings(self, s: str) -> int:
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

        palindrome_count = 0
        for i in range(ROWS):
            for j in range(i, COLS):
                if palindrome(i, j):
                    palindrome_count += 1

        return palindrome_count