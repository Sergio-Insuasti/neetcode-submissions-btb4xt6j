
class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.cap = k
        self.size = 0
        self.arr = [-1] * k
        self.front, self.back = 0, self.cap - 1
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.back = (self.back + 1) % self.cap
            self.arr[self.back] = value
            self.size += 1
            return True
        
        return False
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.arr[self.front] = -1
            self.front = (self.front + 1) % self.cap
            self.size -= 1
            return True
        return False
            
        

    def Front(self):
        """
        :rtype: int
        """
        return self.arr[self.front]
        

    def Rear(self):
        """
        :rtype: int
        """
        return self.arr[self.back]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.cap

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()