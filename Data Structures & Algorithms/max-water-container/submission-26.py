class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # the bottleneck is the height of the smaller bar, andnthe gap between 
        # the current bar and the othe rbar

        # we can have 2 points to do this whole thing in O(n), brute force 
        # would be to consider every pair bars, and find the max area


        # have pointers, and move the pointer according to some 
        # the formula for area

        # yeah so we can just move the right pointer to a new bar is the area 
        # with the new bar is bigger than the current area with the bar setup

        # however, how do we know when to move the left bar

        # if the right pointer height is bigger than the left pointe rheigh
        # move the left pointer so it becomes the new standard

        # so we want to move the bottleneck, the smaller heighet
        # since we just have to return the max volume, no need to track the bars
        # just move the pointers and track the max seen so far

        l = 0
        r = len(heights) - 1
        max_vol = 0

        while l <= r:
            area = min(heights[l], heights[r]) * (r - l)

            max_vol = max(max_vol, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            
        return max_vol







