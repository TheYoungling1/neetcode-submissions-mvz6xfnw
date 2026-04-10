class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        match_1 = float('inf') 
        match_2 = float('inf') 

        # only one pair of index implies that we dont have to worry about
        # uniqueness

        for i in range(0, len(nums)):
            check = target - nums[i]
            if check in nums_set:
                match_1 = i
                match_2 = check

        # Find the index of the match

        for i in range(0, len(nums)):
            if nums[i] == match_2:
                return sorted([match_1, i])
