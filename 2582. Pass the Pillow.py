class Solution:
    def passThePillow(self, n, time):
        # Because the 1-th person has already hold the pillow
        time += 1
        if time <= n :
            return time
        else :
            time -= n

        f = 2*n -2
        number = time % f
        if number <= (n-1) :
            return n - number
        else :
            return number - n + 2


        
        
        