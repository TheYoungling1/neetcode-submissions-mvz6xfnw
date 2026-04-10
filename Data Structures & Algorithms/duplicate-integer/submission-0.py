class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        unique_set = set()

        for num in nums:
            unique_set.add(num)

        if len(unique_set) != len(nums):
            return True
        else:
            return False
        