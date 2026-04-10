import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # so the max eating speed of coco would be the max pile size of the bananas, this would be len(piles)
        # min eating speedd would be one, and this would be sum of all piles

        # iterate from use binary search to find the eating rate from 1 to max?

        left = 1
        right = max(piles)
        min_speed = 0
        while left <= right:
            mid = int((right + left) / 2)

            if self.canFinish(h, piles, mid):
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return min_speed


    
    def canFinish(self, h, piles, speed):
        # O(n)
        time = 0
        for pile in piles:
            print(speed)
            time += math.ceil(pile / speed)

        if time <= h:
            return True
        
        return False