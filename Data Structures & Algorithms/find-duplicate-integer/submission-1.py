class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # int in lengh - 1

        hash_1 = {}

        for num in nums:
            if num not in hash_1:
                hash_1[num] = 1
            else:
                return num