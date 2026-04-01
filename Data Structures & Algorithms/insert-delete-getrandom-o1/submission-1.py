import random
class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.pos = {}
    
    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True
        
    def getRandomNum(self) -> int:
        return random.randint(0, len(self.arr) - 1)

    def remove(self, val: int) -> bool:
        if val not in self.pos: return False

        i = self.pos[val]
        last = self.arr[-1]
        self.arr[i] = last
        self.pos[last] = i

        self.arr.pop()
        del self.pos[val]
        return True
        

    def getRandom(self) -> int:
        idx = self.getRandomNum()
        return self.arr[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()