class Solution:
    def uniquePaths(self, m, n):
        # array[i][j] store the possible unique paths to the point i, j
        # Base case :
        array = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            array[0][i] = 1

        for i in range(m):
            array[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                array[i][j] = array[i - 1][j] + array[i][j - 1]

        return array[m - 1][n - 1]
