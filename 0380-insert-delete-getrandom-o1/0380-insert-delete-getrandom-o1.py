import random

class RandomizedSet:
    def __init__(self):
        self.set_ = set()
        self.list_ = []
        self.mp = {}

    def insert(self, val: int) -> bool:
        if val not in self.set_:
            self.set_.add(val)
            self.mp[val] = len(self.list_)
            self.list_.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.set_:
            idx = self.mp[val]
            last = self.list_[-1]

            self.list_[idx] = last
            self.mp[last] = idx

            self.list_.pop()
            del self.mp[val]
            self.set_.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        n = len(self.set_) - 1 
        idx = random.randint(0, n)
        return self.list_[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()