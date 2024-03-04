import random
class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.hashmap = dict()
        self.n = 0

        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            return False
        

        self.nums.append(val)
        self.hashmap[val] = self.n 
        self.n += 1

        return True

        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap :
            return False

        # Swap val to the last element, then pop last with O(1)

        idx = self.hashmap[val]
        last_ele = self.nums[-1]
        
        # SWAP
        self.nums[idx] = last_ele
        self.hashmap[last_ele] = idx

        # POP LAST
        remover = self.nums.pop()
        del self.hashmap[val]
        self.n -= 1

        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        idx = random.randint(0, self.n - 1)
        

        return self.nums[idx]      


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()