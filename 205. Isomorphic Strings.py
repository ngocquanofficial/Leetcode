class Solution:
    def isIsomorphic(self, s, t):
        s = list(s)
        t = list(t) # convert s, t from strings to str lists
        
        domain = set(s)
        domain = list(domain) # the order is not important
        image = []
        
        for x in domain :
            index = s.index(x)
            image.append(t[index])
        
# Due to the condition 'No two characters may map to the same character'
        if len(image) != len(list(set(image))) :
            return False
        
        for i in range(len(s)) :
            x = s[i] # the domain point
            
            if t[i] != image[domain.index(x)] :
                return False
        
        return True
    
