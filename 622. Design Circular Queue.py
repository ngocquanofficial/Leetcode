class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.data = [None]* k # k-element list
        self.k = k
        self.head = -1
        self.tail = -1
        # When both head and tail = -1, mean empty Queue
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull() :
            return False
        if self.isEmpty() :
            self.tail = 0
            self.head = 0
            self.data[0] = value
            return True        
        #ELSE
        self.tail = (self.tail + 1) % self.k
        self.data[self.tail] = value

        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty() :
            return False
        
        #ELSE

        if self.head == self.tail :
            # After removing, become empty queue
            self.tail = -1
            self.head = -1
            return True

        self.head = (self.head + 1) % self.k
        return True
        
        
            
        

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty() :
            return -1
        return self.data[self.head]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty() :
            return -1
        return self.data[self.tail]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return (self.head == -1 and self.tail == -1)
        

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.head == (self.tail + 1) % self.k) 
        


