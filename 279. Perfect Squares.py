import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        

        queue = []
        visited = set()
        step = 0

        queue.append(n)
        visited.add(n)
        target = 0


        def adjacent(n) :
            max_sqrt = int(math.sqrt(n))
            return [n - i**2 for i in range(max_sqrt, 0, -1)]

        while len(queue) > 0 :
            for i in range(len(queue)) :
                current = queue.pop(0)
                visited.add(current)

                if current == target :
                    return step
                
                adj_list = adjacent(current)
                for num in adj_list :
                    if num not in visited :
                        queue.append(num)
                        visited.add(num)

            step += 1                


obj = Solution()
n = int(input())
print(obj.numSquares(n))




