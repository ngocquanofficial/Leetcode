class Solution:
    def longestPalindrome(self, s) :
        unique_element = list(set(s))
        longest = 0
        odds = []
        for letter in unique_element :
            number = s.count(letter)
            
            if number % 2 == 0 :
                longest += number
            else :
                odds.append(number)

        if len(odds) == 0 :
            return longest    

        elif len(odds) == 1 :
            longest += odds[0]
        else :
            # Expect the largest element in odds, we use odds[i]-1 is a even number
            total = sum(odds[:-1]) - len(odds[:-1]) + odds[-1]
            longest += total 

        return longest