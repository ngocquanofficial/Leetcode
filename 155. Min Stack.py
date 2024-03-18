class MinStack(object):

    def __init__(self):
        self.min_stack = []
        self.nums = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.nums == [] :
            self.min_stack.append(val)
        else :
            if val > self.min_stack[-1] :
                self.min_stack.append(self.min_stack[-1])
            else :
                self.min_stack.append(val)

        # Update nums
        self.nums.append(val)


        

    def pop(self):
        """
        :rtype: None
        """
        remover = self.nums.pop()
        _ = self.min_stack.pop()
        pass
        

    def top(self):
        """
        :rtype: int
        """
        return self.nums[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()