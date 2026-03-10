class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.k = k
        self.value = value
        self.last = -1

    def consec(self, num: int) -> bool:
        self.stream.append(num)

        if num != self.value:
            self.last = len(self.stream) - 1
        
        if len(self.stream) < self.k:
            return False

        if len(self.stream) > self.k:
            self.stream.popleft()
            self.last -= 1

        return self.last < 0


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)