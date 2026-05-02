class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # brute force


        # Input: text1 = "cat", text2 = "crabt" 
        # i = c, j = c
        # yes, move i = a, j = r
        # no match, try recurse on moving i = t, and j = a

        #...

        dp_list = {}

        def recurse(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if i in dp_list and j in dp_list[i]:
                return dp_list[i][j]

            dp_list.setdefault(i, {})

            if text1[i] == text2[j]:
                dp_list[i][j] = 1 + recurse(i + 1, j + 1)
            else:
                dp_list[i][j] = max(recurse(i + 1, j), recurse(i, j + 1))

            return dp_list[i][j]

        return recurse(0, 0)
                