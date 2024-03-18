class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        digits = {"0","1", "2", "3", "4", "5", "6", "7", "8", "9"}

        for char in s :

            if char != "]" :
                stack.append(char)
                continue

            # ELSE when char= "]"
            letters = ''
            while stack[-1] != "[" :
                letter = stack.pop()
                letters = letter + letters


            _ = stack.pop() # _ = "["

            # begin to iterate over nums

            nums = ''
            while stack and stack[-1] in digits :
                num = stack.pop()
                nums = num + nums

            stack.append(int(num) * letters)

            print(int("".join(nums)))

        return "".join(stack)



s = "10[leetcode]"

obj = Solution()
print(obj.decodeString(s))





            
            

