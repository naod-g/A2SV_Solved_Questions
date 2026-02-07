class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.counter = defaultdict(int)

    def add(self, number: int) -> None:
        f = self.freq[number]
        if f > 0:
            self.counter[f] -= 1
        self.freq[number] += 1
        self.counter[f+1] += 1

    def deleteOne(self, number: int) -> None:
        f = self.freq[number]
        if f == 0:
            return
        self.freq[number] -= 1
        self.counter[f] -= 1
        if f - 1 > 0:
            self.counter[f - 1] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.counter[frequency] > 0



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)