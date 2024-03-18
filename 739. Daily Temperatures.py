class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        answer = [0] * len(temperatures)

        for idx, current in enumerate(temperatures) :
            while True :
                if stack == [] : # all previous index has correct values
                    stack.append((idx, current))
                    break
                
                # ELSE
                # only get value, NOT pop
                last_idx, last_pop = stack[-1]


                if current <= last_pop :
                    stack.append((idx, current))
                    break

                # here, current idx is the first warmer day of last-idx day

                answer[last_idx] = idx - last_idx
                # POP the last value in stack 
                _ = stack.pop()

        # all value remaining has no warmer day in future, then receive default value = 0
        return answer
    

obj = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(obj.dailyTemperatures(temperatures))
                    
                




