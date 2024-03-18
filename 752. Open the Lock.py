import itertools

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        deadends_set = set()
        for string in deadends :
            deadends_set.add(string)

        queue = []
        visited = set()
        queue.append("0000")
        visited.add("0000")
        step = 0

        def adjacent(key) :
            adjacent_list = []
            for i in range(len(key)) :
                digit = key[i]
                int_digit = int(digit)
                adj = [str((int_digit-1)%10), str((int_digit+1)% 10)]
                for t in adj :
                    adjacent_list.append(key[:i] + t + key[i+1:])

            return adjacent_list



        while len(queue) > 0 :
            for i in range(len(queue)) :
                current = queue.pop(0)
                if current in deadends_set :
                    continue


                if current == target :
                    return step
                
                adj_list = adjacent(current)
                for adj in adj_list :

                    
                    if adj not in visited :
                        visited.add(adj)
                        queue.append(adj)

            step += 1

        return -1

dead_ends =["0201","0101","0102","1212","2002"]
target = "0202"

obj = Solution()
print(obj.openLock(deadends= dead_ends, target= target))