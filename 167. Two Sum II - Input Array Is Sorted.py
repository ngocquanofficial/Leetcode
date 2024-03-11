class Solution(object):
    # BY MY SELF
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        n = len(numbers)
        first = 0
        second = n - 1
        while True :
            current = numbers[first] + numbers[second]

            if current == target :
                return [first + 1, second + 1]
            
            if current < target :
                first += 1
            
            else : # current > target
                second -= 1