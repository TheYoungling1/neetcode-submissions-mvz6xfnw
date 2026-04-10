class MinStack:

    def __init__(self):
        self.list = deque()
        self.min_list = deque()

    def push(self, val: int) -> None:
        self.list.append(val)
        if not self.min_list:
            self.min_list.append(val)
        else:
            self.min_list.append(min(self.min_list[-1], val))

        return None

    def pop(self) -> None:
        self.list.pop()
        self.min_list.pop()
        return None
    
    # at every push, find the min between the already existing min to the current val

    def top(self) -> int:
        return self.list[-1]
        

    def getMin(self) -> int:
        return self.min_list[-1]
        
