class Solution:
    def bestClosingTime(self, customers):
        current = 0
        past = 0
        minimum_day = 0
        minimum_penalty = current
        for i in range(1, len(customers)):
            if customers[i - 1] == "Y":
                current = past - 1
            elif customers[i - 1] == "N":
                current = past + 1

            if current < minimum_penalty:
                minimum_day = i
                minimum_penalty = current
            past = current

        # Special case: store only close after n hours
        if minimum_penalty < current:
            return minimum_day

        if customers[-1] == "Y":
            return len(customers)
        else:
            return minimum_day
