class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) this means I cant sort it

        # 2 pointer problem, move the pointer if the pointed element is less than the current

        nums_set = set(nums)

        print(nums_set)

        # find the lowest

        # For each num in the set, see if its neighours is in the set too
        if len(nums_set) == 0:
            return 0

        starters = []
        for num in nums_set:
            if num - 1 not in nums_set:
                starters.append(num)

        longest = 0
        for starter in starters:
            length = 1
            while starter + length in nums_set:
                length += 1
            longest = max(length, longest)
        
        return longest

        
        # find the union of all the different sets
        

        
        return length 