class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        # the decision tree starts with each individual num
        # then add a num not in in current branch yet
        # skips duplicates along the way, sort the array first


    #                         [ ]
    #           ┌──────────────┼──────────────┐
    #           │              │              │
    #         [1]           [1] ✗            [2]
    #      (i=0)         (skip i=1)        (i=2)
    #       /  \                            /  \
    #    [1,1] [1,2]                    [2,1] [2,1] ✗
    #    (i=1) (i=2)                    (i=0) (skip i=1)
    #     |     |                        |
    #   [1,1,2][1,2,1]                 [2,1,1]


        res, n = [], len(nums)
        visit = [False] * n
        perm = []

        def dfs():
            if len(perm) == n:
                res.append(perm.copy())
                return

            for i in range(n):
                if visit[i]:
                    continue

                if i and nums[i] == nums[i - 1] and not visit[i - 1]:
                    continue
                visit[i] = True
                perm.append(nums[i])
                dfs()
                visit[i] = False
                perm.pop()

        nums.sort()
        dfs()
        return res