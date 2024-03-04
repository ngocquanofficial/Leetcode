class TwoSum(object):

    def __init__(self):
        self.hashmap = dict()

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.hashmap :
            self.hashmap[number] += 1
            return
        # ELSE
        self.hashmap[number] = 1
        

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """

        for num in self.hashmap :
            
            # BASE CASE : target = 2 * num
            if value == 2 * num :
                if self.hashmap[num] >= 2 :
                    return True
                continue
            
            if value - num in self.hashmap :
                return True
            
        return False

    

        


# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
number = 0
obj.add(number)
obj.add(0)
param_2 = obj.find(0)
    
    