class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        max_diagonal = m - 1 + n - 1
        travel_order = []



        for line in range(max_diagonal + 1) :
            
            # ODD LINE, then column decrease
            if line % 2 == 1 :
                # PROVE: 
                # 0 <= row <= m - 1
                # 0 >= -row >= - (m - 1)
                # line >= line - row = column >= line - (m-1)
                # Then we iterate column from min(line, n - 1) to max(0, line - (m - 1) )
                for column in range(min(line, n - 1), max(0, line - (m-1)) - 1, -1) :
                    row = line - column
                    ele = mat[row][column]

                    travel_order.append(ele)

            else :
            # EVEN LINE, then row decrease
                for row in range(min(line, m - 1), max(0, line - (n-1)) - 1, -1) :
                    column = line - row
                    ele = mat[row][column]
                    travel_order.append(ele)

        return travel_order
           