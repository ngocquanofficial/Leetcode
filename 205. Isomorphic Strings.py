# Created by NgocQuanNE, 2023-01-17

def isIsomorphic(s, t) :
    s = list(s)
    t = list(t) # convert s, t from strings to str lists
    # Idea:Isomorphic if and only if we can build a bijective from s to t
    # consider s as domain list, t as image list
    
    domain = set(s)
    domain = list(domain) # the order is not important
    image = []
    
    for x in domain :
        index = s.index(x)
        image.append(t[index])
        
    # we called the bijective from s to t, which is created above, as f(x)
    
    # then, we check whether f(s) == t
    
    if len(image) != len(list(set(image))) :
        return False
    
    for i in range(len(s)) :
        x = s[i] # the domain point
        
        if t[i] != image[domain.index(x)] :   # check the element in t with the associate image created by f(x)
            return False
    
    return True

s = "badc"
t = "baba"
print(isIsomorphic(s, t))    
    