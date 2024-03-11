class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        if len(digits) == 1 :
            if digits[0] == 9 :
                return [1, 0]
            else :
                return [digits[0] + 1]
        
        if digits[-1] != 9 :
            
            digits[-1] = digits[-1] + 1
            return digits
        else :
            return self.plusOne(digits[:-1]) + [0]
        