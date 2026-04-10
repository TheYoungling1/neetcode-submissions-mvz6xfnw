class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # We want long bar as well as being far away

        # volume at any time is the least tall bar * current 2 pointer distance

        # if the next bar is bigger than current bar, we move the left pointer,

        # right pointer keeps iterating forward and find the a larger area

        # left = 0
        # right = 1
        # area = 0

        # #keep curr max
        # max_idx = 0
        
        # while right < len(heights):
        #     curr = min(heights[left], heights[right]) * (right - left)
        #     print(heights[left], heights[right], max_idx, area)

        #     if heights[right] > heights[max_idx]:
        #         max_idx = right
        #     if curr > area:
        #         area = curr
        #         # if the height is less than curr and higher in index
        #         # then no way it can be higher than if we keep left here
        #         tmp = min(heights[max_idx], heights[right]) * (right - max_idx)
        #         print("temp: ", tmp)
        #         if tmp > area:
        #             left = max_idx
        #             area = tmp

                
        #     right += 1
        
        # return area

        # keep the width maximised first

        left = 0
        right = len(heights) - 1

        area = 0

        while left < right:
            curr = min(heights[left], heights[right]) * (right - left)
            if curr > area:
                area = curr

            # try to move to a better place,

            # move the shorter height try to stop the bottleneck

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
            

        return area


