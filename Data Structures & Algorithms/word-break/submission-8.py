class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # recurse(i) if s[i:] can be constructed from words in wordDict

        # recurse(len(s)) return 0

        # the question can be split into 2 parts
        # assume that there is only one word betwen i and the end of string s
        # at index i, can the word from s[0:i] be constructed from worddict
        # and if there is a word in word dict that can fill from i to len(s)

        memo = {len(s) : True}

        def recurse(i):            
            if i in memo:
                return memo[i]

            for w in wordDict:
                if (i + len(w) <= len(s) and s[i: i + len(w)] == w
                ):
                    if recurse(i + len(w)):
                        memo[i] = True
                        return True
                    
            memo[i] = False
            return False

        return recurse(0)


        