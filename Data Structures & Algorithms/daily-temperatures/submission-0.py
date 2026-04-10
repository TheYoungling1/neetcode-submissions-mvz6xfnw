class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force is O(n^2) for each temperature, cycle through
        # the rest of the array to find the bigger temp

        # As we are looking for the future dates? we want to construct 
        # the DS backwards?

        # the DS is initially empty

        # so when we add 28, there will be nothing to compare to, 0 

        # when we add 40, it will compare with 28

        # 28 smaller than 40, so 0 as well

        # up to 35, the stack should be 40 -> 28

        # to add 35 to the array, we need to pop 40, and add 35

        # use a stack because we are finding the first day thats warmer

        # but thats still O(n^2)


        # monotonic increasing stack

        # stack grows from bottom up

        # 28
        # 40 -> 28
        # 40 -> 35

        # what about tracking indices

        # 6
        # 5 -> 6
        # 5 -> 4
        # 5 -> 3
        # 5 -> 3 -> 2

        # the bottom is always the element closer

        # if a number bigger than indice 5 is at indice 1, then no num 
        # ahead of it, so its result is 0, but this means all nums before 
        # it can just choose indice 1 instead of something later in the array

        # at all times, the head is the current value, and the rest of the array
        # the elements bigger even bigger than it

        # so if we meet a smaller number, then thats fine, we can add it as head
        # and compare indices with the old head thats means the next element is 
        # already bigger than it

        # if we need to delete anything, i.e. the curr element is bigger 
        # than the old head, find the indice of the first element thats bigger than 
        # the curr element, and make the curr element the head
        # i.e. for all elements before curr, then can just compare to curr,
        # as curr is both closer as well as bigger than the old head so no
        # conflict value

        stack = deque()
        results = [0] * len(temperatures)
        for j in reversed(range(len(temperatures))):
            while stack:
                element = stack[-1]        # peek top
                if temperatures[element] > temperatures[j]:
                    break                  # keep this element on the stack
                stack.pop()                # safely pop

            if stack:
                results[j] = stack[-1] - j
            else:
                results[j] = 0

            stack.append(j)
        
        return results











