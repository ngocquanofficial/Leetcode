# Problem: 926. Flip String to Monotone Increasing

class mySolution:
    def minFlipsMonoIncr(self, s) :
        first_one = s.find('1')
        last_zero = len(s) - 1 - s[::-1].find('0') # change to real index in origin s, not index in s reverse
        # Base case 
        if len(s) == 1 :
            return 0
        if first_one == -1 or last_zero == len(s) :
            return 0
        if first_one != 0 or last_zero != len(s) - 1 :
            return mySolution.minFlipsMonoIncr(self, s[first_one:last_zero+1])
        
        # We deal with case in which first element is 1, last element is 0
        
        first_zero = s.find('0') # When 11.111 at the beginning, if need to change, we must change all of them
        last_one = len(s) - 1 - s[::-1].find('1') # similar for zeros in the end
        
        change_1 = mySolution.minFlipsMonoIncr(self, s[first_zero:]) + first_zero # first one is the number of 0 at begining
        change_0 = mySolution.minFlipsMonoIncr(self, s[:last_one+1]) + (len(s)-1) - last_one  # plus the number of 1 at the end
        return min(change_0, change_1)

        
        
        
        
