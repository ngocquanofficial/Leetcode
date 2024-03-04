class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        history_set = set() # map x -> f(x) = sum of square of digit of x
        
        while n != 1 :

            fn = self.f(n)

            if fn == 1 :
                return True

            if fn in history_set :
                return False
            else :
                history_set.add(fn)
                n = fn
        
        return True # when n = 1, but for some reason it was not returned in while loop

    def f(self, n) :
        digit_square = [int(i)**2 for i in list(str(n))]

        return sum(digit_square)
        

## SECOND SOLUTION: USING SLOW/FAST POINTER APPROACH
class Solution1(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 :
            return True
        slow = self.f(n)
        fast = self.f(self.f(n))
        while True :
            if slow == 1 or fast == 1 :
                return True
            if slow == fast : # Therefore, exists a cycle
                return False
            slow = self.f(slow)
            fast = self.f(self.f(fast))


    def f(self, n) :
        sum_quare = 0
        while n > 0: 
            sum_quare += (n % 10)** 2
            n = n // 10
        return sum_quare
    

obj = Solution1()
print(obj.isHappy(n= 2))
