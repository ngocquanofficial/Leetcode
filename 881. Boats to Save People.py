class Solution:
    def numRescueBoats(self, people, limit):
        n = len(people) - 1 # index of the last element
        # BASE CASE
        if n == -1 : # people is a empty set
            return 0
        if n == 0 :
            return 1
        people = sorted(people)
        i = 0
        count = 0
        while n > i :
            if people[n] + people[i] > limit :
                n -= 1 # can not served people[n] with another person in only 1 boat
                count += 1 # the boat serves exactly people[n]
            else : # when people[n] and people[i] can be served by 1 boat
                n -= 1
                i += 1
                count += 1
                
        if n == i : 
            count += 1 # boat serves people[n = i]
            
        return count
                