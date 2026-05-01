class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return nums

        n = len(nums)
        r = k % n
        print(r)
        print(n)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        # 8 7 6 5 4 3 2 1
        print(nums)
        reverse(0, r - 1)
        reverse(r, n - 1) 