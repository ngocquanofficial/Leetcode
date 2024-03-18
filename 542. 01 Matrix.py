class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        ans = [ [0 for i in range(n)] for i in range(m)]
        visited = set()
        my_queue = []

        for row in range(m) :
            for col in range(n) :
                if mat[row][col] == 0 :
                    visited.add((row, col))
                    my_queue.append((row, col))

        def adjacent(row, col) :
            adj_list = [(row, col + 1), (row, col - 1), (row+1, col), (row-1, col)]
            shortlist = []
            for adj in adj_list :
                r, c = adj
                if (r < 0) or (r == m) or (c < 0) or (c == n) :
                    continue
                shortlist.append((r, c))

            return shortlist
                 

        step = 0

        while len(my_queue) > 0 :
            for i in range(len(my_queue)) :
                row, col = my_queue.pop(0)
                ans[row][col] = step
                adj_list = adjacent(row, col)
                for adj in adj_list :
                    if adj not in visited :
                        my_queue.append(adj)
                        visited.add(adj)

            step += 1

        return ans


        