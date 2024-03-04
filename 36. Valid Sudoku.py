
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        row_sets = [set() for i in range(9)]
        column_sets = [set() for i in range(9)]
        grid_sets = [set() for i in range(9)]

        for row in range(9) :
            for column in range(9) :
                ele = board[row][column]

                if ele == "." :
                    continue
                # ELSE

                # check for unique in row, column, grid

                if ele in row_sets[row] :
                    return False
                else :
                    row_sets[row].add(ele)

                if ele in column_sets[column] :
                    return False
                else :
                    column_sets[column].add(ele)
                
                grid_index =  3 * (row // 3 ) + column // 3


                if ele in grid_sets[grid_index] :
                    return False
                else :
                    grid_sets[grid_index].add(ele)

                
        return True



        