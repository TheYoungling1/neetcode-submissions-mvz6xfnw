class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # if we visualize this as a decision tree, then, the top layer would be the letters of 3, then 4... etc... 

        # we can just append the snapshot of the path, then backtrack then add to the res array

        if len(digits) == 0:
            return []


        res, path = [], []
        

        map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(i):
            if i == len(digits):
                res.append("".join(path))
                return


            for letter in map[digits[i]]:
                path.append(letter)
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return res 