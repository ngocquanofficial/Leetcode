import queue

class MovingAverage:

    def __init__(self, size: int):
        self.data = queue.Queue(maxsize= size)
        self.sum = 0
        self.size = size
        self.len = 0

        

    def next(self, val: int) -> float:
        if self.data.full() :
            remover = self.data.get()
            self.data.put(val)
            self.sum = self.sum + val - remover
            return self.sum / self.len
        
        # ELSE: queue not full
        self.data.put(val)
        self.len += 1
        self.sum += val
        return self.sum/ self.len
        
        