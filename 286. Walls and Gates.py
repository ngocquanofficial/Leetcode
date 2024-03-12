import queue

class Solution:
    def add_item(self, *coor) :
        for r, c in coor:
            if (r < 0) or (c < 0) or (r == self.m) or (c == self.n) or self.rooms[r][c] == -1 :
                continue # Not add to queue
            
            # ELSE
            if (r,c) not in self.visited :
                self.queue.append((r, c))
                self.visited.add((r,c))
    
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        self.m, self.n = len(rooms), len(rooms[0])
        self.rooms = rooms

        # Initialize queue, visited
        self.queue = []
        
        self.visited = set()
        # first add all the gate to queue
        for row in range(self.m) :
            for col in range(self.n) :
                if rooms[row][col] == 0 :
                    self.queue.append((row, col))
                    self.visited.add((row, col))
        
        distance = 0

        while len(self.queue) > 0 :
            # each time, iterate all cell that has shortest distance to gate = distance
            for i in range(len(self.queue)) :
                (r, c) = self.queue.pop(0)

                # if not assign shortest distance
                # if (r, c) not in self.visited :
                self.rooms[r][c] = distance
                self.visited.add((r, c))

                self.add_item((r+1, c), (r-1, c), (r, c+ 1), (r, c-1))



            # After visiting all cells with shortest dis = distance
            distance += 1

        return self.rooms


rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

obj = Solution()
print(obj.wallsAndGates(rooms))



        
        