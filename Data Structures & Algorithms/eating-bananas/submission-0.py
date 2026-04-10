class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #O(nlogm) n is the size of piles, m is the max value in array

        # what about for each value, round it up?
        # h is always longer than the pile banana

        #  the shortest time, h = len(piles)
        # k = max(piles)

        # least bananas eat per hour, h = total number of bananas 
        # k = 1


        # if I have 4 hours, and 4 piles, then k = max(piles) becausse i must
        # finished the max pile in one go

        # if I have 8 hours, and 4 piles, then we can just go k = 1/2 max(piles)
        # we can finished the max piles in 2 go


        # So we just iterate k from 1 to max(piles)

        # we know that if k = x works, then k = x + 1 works and everything 
        # bigger than x will also work

        #given that m is way larger than n, we need to use binary 
        # search, iteratively halfing until we find the first k that works
        

        left = 1
        right = max(piles)

        curr_min = max(piles)

        while left <= right:
            middle = (right + left) // 2
            print(middle)
            print(self.can_finish(piles, h, middle))
            if self.can_finish(piles, h, middle):
                curr_min = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return curr_min


    def can_finish(self, piles, h, k):
        count = 0
        for num in piles:
            if num <= k:
                count += 1
            else:
                count += num // k
                if num % k != 0:
                    count += 1

            if count > h:
                return False
        
        return True