class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        # element of stack is [idx, temp], which is temparatures and index of its day
        answer = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                # compare with the temp of the last element in stack, when stack is not empty

                answer[stack[-1][0]] = idx - stack[-1][0]  # index of day at stack[-1]
                stack.pop()  # pop this day after assign its value to answer array
                # Then, continue loop until stack is a non-increasing array

            # Add this day to stack, we ensure that its temp is smallest when compare to
            # other days in stack
            stack.append([idx, temp])

        return answer
