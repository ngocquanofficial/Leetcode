class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # IDEA: When travel 1 round with 4 edge of matrix, the remaining way is the same as the full way of the (m-2) * (n-2) matrix

        # Then we have 4 base case: 1 row, n-m + 1 column; 2 row, n-m+2 column; m-n+1 row, 1 column; m-n+2 row, 2 column
        m = len(matrix)
        n = len(matrix[0])

        if m == 1 :
            return matrix[0]
        elif m == 2 :
            return matrix[0] + list(reversed(matrix[1]))
        
        elif n == 1 : # 1 column
            element = [i[0] for i in matrix]
            return element
        
        elif n == 2 : # and m > 2 
            first_row = [i[0] for i in matrix]
            second_row = [i[1] for i in matrix]

            return [first_row[0], second_row[0]] + second_row[1: -1] + [second_row[-1], first_row[-1]] + list(reversed(first_row[1: -1]) )

        else :
            last_row = [i[-1] for i in matrix]
            first_row = [i[0] for i in matrix]

            outer_element = matrix[0] + last_row[1: -1] + list(reversed(matrix[-1]) )+ list(reversed(first_row[1: -1]) )

            del matrix[0]
            del matrix[-1]

            for r in matrix :
                del r[0]
                del r[-1]
            
            return outer_element + self.spiralOrder(matrix)
        
