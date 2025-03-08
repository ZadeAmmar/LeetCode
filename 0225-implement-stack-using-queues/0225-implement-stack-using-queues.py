class MyStack(object):
    def __init__(self):
        self.arr = []
        self.n = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.arr.append(x)
        self.n += 1

    def pop(self):
        """
        :rtype: int
        """
        if self.n <= 0:
            return None
        self.n -= 1
        return self.arr.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.n <= 0:
            return None
        return self.arr[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.n == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()