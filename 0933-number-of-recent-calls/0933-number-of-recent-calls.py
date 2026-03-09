class RecentCounter:

    def __init__(self):
        self.a = deque()

    def ping(self, t: int) -> int:
        while self.a and self.a[0] < t-3000:
            self.a.popleft()

        self.a.append(t)

        return len(self.a)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)