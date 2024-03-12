class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid :
            return 0
        
        m, n = len(grid), len(grid[0])

        visited = set()
        island = 0

        def bfs(row, col) :
            queue = [(row, col)]
            visited.add((row, col))

            while len(queue) > 0 :
                for i in range(len(queue)) :
                    row, col = queue.pop() 
                    adjacent_list = [(row,col+1), (row, col-1), (row-1, col), (row+1, col)]

                    for (r,c) in adjacent_list :
                        # Check for valid index 
                        if (r < 0) or (r == m) or (c < 0) or (c == n) :
                            continue

                        # if node is a land and not visited
                        if (r,c) not in visited and grid[r][c] == "1" :
                            queue.append((r,c))
                            visited.add((r,c))
                    



        for row in range(m) :
            for col in range(n) :
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    # bfs and mark all adjacent lands become visited
                    island += 1

        return island


obj = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

print(obj.numIslands(grid))