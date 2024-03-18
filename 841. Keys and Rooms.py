class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        visited = set()
        visited.add(0)
        stack = []
        stack.append(0)
        while len(stack) > 0 :
            idx = stack.pop()
            adj_list = rooms[idx]
            for adj in adj_list :
                if adj not in visited :
                    visited.add(adj)
                    stack.append(adj)
            
        return len(visited) == n
        