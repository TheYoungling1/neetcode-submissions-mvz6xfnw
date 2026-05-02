class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        part = []

        def backtrack(i):
            if i > n:
                if len(part) == k:
                    res.append(part.copy())
                return

            part.append(i)
            backtrack(i + 1)
            part.pop()
            backtrack(i + 1)

        backtrack(1)
        return res