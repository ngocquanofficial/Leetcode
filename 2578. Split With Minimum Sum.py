class Solution:
    def splitNum(self, num):
        digits = [int(i) for i in list(str(num))]
        digits = sorted(digits)
        maximum = 0
        exp = 0
        while digits :
            first = digits.pop()
            second = 0
            if digits :
                second = digits.pop()
            maximum += (first + second) * 10**exp
            exp += 1
            
        return maximum
    
