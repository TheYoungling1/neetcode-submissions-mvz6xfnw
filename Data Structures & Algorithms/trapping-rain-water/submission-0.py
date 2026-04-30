class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointers

        # the max water stored is depending on the smaller bar
        # we can keep moving thr right pointer to only when  we find a bar
        # >= left pointe bar, because we know that even if there is a bigger 
        # bar after that, it will be bottlenecked by the smaller bar, so its
        # easier to fill the smaller gap first
        
        # also want to make sure that there is a 0 between the bar elements


        # the amount water we can hold at one element i
        # is min(leftmax, rightmax) + height[i]
        # leftmax is the max left bar seen so far, and rightmax, is the max
        # right bar seen so far


        l = 0
        r = len(height) - 1
        l_max = height[0]
        r_max = height[r]
        total = 0

        if l_max < r_max:
            i = l
        else:
            i = r

        while l < r:
            if height[l] < height[r]:
                a = min(l_max, r_max) - height[l]
                l += 1
                i = l
            else:
                a = min(l_max, r_max) - height[r]
                r -= 1
                i = r
            
            if a > 0:
                total += a
                
            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)
        
        return total



