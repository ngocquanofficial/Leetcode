class Queue() :
    def __init__(self) :
        self.data = []
        self.position = 0 # The first position remaining in queue

    def en_queue(self, num) :
        self.data.append(num)
        return True

    def is_empty(self) :
        return self.position >= len(self.data)

    def de_queue(self) :
        if not self.is_empty() :
            self.position += 1
            return self.position - 1 # prev position
        print("The Queue is empty, can not remove")
        return False
    
    def get_position(self) :
        return self.position
    
    def __str__(self) :
        return f"{self.data[self.position:]}"
    

my_queue = Queue()
my_queue.en_queue(5)
my_queue.en_queue(10)
print(my_queue)
my_queue.de_queue()
print(my_queue)
my_queue.de_queue()
my_queue.de_queue()
print(my_queue)
        
    