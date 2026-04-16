import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # sort the array with a lambda funciton in python 
        # O(nlogn) 

        # get the first k elements of that array

        # for each point, we just calculate its distance from the origin

        # we find the kth's smallest point in that list

        # however, since we are returnning the actual point, we have to have a hashmap of the distance -> the point, which works. because we can return any order
        # of points given that they have th same distance

        # One for loop in O(n) that finds the distance, and map the distance to points in a hashmap

        # heapify this into a min heap, so the head of this heap can be called the "n'th" closest point

        # graudally pop the head of this heap (and re-org) k times, and we will get the k smallest distance

        # min_heap = []

        # for point in points:
        #     dist = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
        #     print(dist)

        #     heapq.heappush(min_heap, (dist, point))
        
        # res = []
        # for i in range(0, k):
        #     point = heapq.heappop(min_heap)

        #     res.append(point[1])

        # return res

        # k*log(n)


        # what about a n*log(k) approach

        # a min heap of size k? but getting to know that a point is bigger than the smallest distance does not help us in finding the k smallest

        # however, if we maintain a max heap of size k, if you are smaller than the current biggest known value in the k-heap. then you get in


        max_heap = []

        for point in points:
            # minus the values by -1 to make into a max_heap so the k-th largest in the max heap = the k-th smallest in the min-heap
            dist = -math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            print(dist)

            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, point))
            else:
                if dist > max_heap[0][0]:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (dist, point))

        res = []        
        for point in max_heap:
            res.append(point[1])

        return res
