class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        marks = list(s)
        pair = {"[": ']', "(": ')', "{": '}'}
        open_mark = ('[', '{', '(')
        close_mark = (']', '}', ')')
        
        stack = []

        for mark in marks :
            if mark in open_mark :
                stack.append(mark)
                continue

            # ELSE mark in close
            if stack == [] :
                return False
            
            last_open = stack.pop()

            if mark != pair[last_open] :
                return False
            # else continue

        return stack == []
            
