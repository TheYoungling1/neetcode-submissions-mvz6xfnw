class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # brute force:
        # for each car, calculate all of itss possible locations
        # and then, check each car see if there is a intersection in the 2 position arrays

        # find the difference between the positionss, the difference between the speed, and the difference between the largest
        # position to the target

        # sort the tuples by the time it takes to arrive to the tagretr

        # so for one car, the time it takes to reach the target will be round_up((target - pos) / speed)

        # example 2: 

        # car 1 (10-4) / 2 = 3 
        # car 2 (10-1) / 2 = 5
        # car 3 (10 - 0) / 1 = 10
        # car 4 (10 - 7) / 1 = 3

        # What if the cars meet before the target

        # target 10, possition = [0, 4], speed = [4, 2]
        # they should meet at 8

        # car 1 = (10 - 0) / 4 = 3
        # car 2 = (10 - 4) / 2 = 3

        # this means that car_1 will reach the end before car 2, but at some point it would have overtaken car 2 
        # so they would have been arriving at the target in the same speed, so in the same fleet
        
        cars = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            car = (position[i], time)
            cars.append(car)

        
        sorted_cars = sorted(cars, reverse=True)        
        print(sorted_cars)

        # if the cars that's later than the cars before but still arrives in the same ticks, then they will intersect at ssome point, making them arrive in a fleet

        # make a sstack, and for each  car, remove the cars from that stack that
        
        stack = deque()
        for car in sorted_cars:
            # the top of the stack means the car with the slowest time on arrival, because this, even if the car furtherest away has the fastest time, it will still be 
            # block by the car ahead of it
            if len(stack) == 0:
                stack.append(car)
            elif car[1] > stack[-1][1]:
                stack.append(car)



        return len(stack)

