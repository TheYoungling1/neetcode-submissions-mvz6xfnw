class Solution:
    def numDecodings(self, s: str) -> int:
        # 1 + recursion on the string 2 to len(s)
        # 1 + recurse(012)
        # 10 + recurse(12)

        # if invalid, we can just respond with something negative

        # like 01 will return something -inf, and when we add to the q

        # since each code is at most 2 digits

        # recurse(1) + recurse(2)
        # but how do we reflect that 01/02 results in no valid combinations at all?
        n = len(s)
        memo = [-1] * (n + 1)   # -1 = "not computed yet"
        
        def recurse(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if memo[i] != -1:
                return memo[i]
            
            ways = recurse(i + 1)
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                ways += recurse(i + 2)
            
            memo[i] = ways
            return ways
        
        return recurse(0)



