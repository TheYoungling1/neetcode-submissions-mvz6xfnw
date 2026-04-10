class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # A hashmap to keep track the number of times a character has appeared

        # O(n)

        # then run k times to find the k highest values in the hashmap?
        # However, this will be terrible as K grows larger


        #Another option, use a hashmap the same way, but, construct a max heap tree 
        # to store the frequencies of each character

        # Then use the max heap to extract the k largest frequencies,

        # then just search these indicies for the actual chars?
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 0
            map[num] += 1

        print(map)
        
        arr = [[] for _ in range(len(nums) + 1)]  # Independent lists; +1 for max freq
        
        # Fill buckets ONCE per unique num
        for num, freq in map.items():
            arr[freq].append(num)


        print(arr)
        
        result = []
        for i in reversed(range(len(arr))):
            if arr[i]: # If the bucket isn't empty
                result.extend(arr[i])
            
            # Stop early if we have enough elements
            if len(result) >= k:
                break
        return result[:k]





