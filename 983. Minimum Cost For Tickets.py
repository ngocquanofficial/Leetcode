class Solution:
    def mincostTickets(self, days, costs):
        minimum_money = [0] * (
            days[-1] + 1
        )  # from day 1 to day 365, not consider the first element

        # minimum_money[i] is the min money spend for traveling from day 1 to the day i

        # Dynamic Programming Approach

        for i in range(1, len(minimum_money)):
            if i not in days:
                minimum_money[i] = minimum_money[i - 1]
            else:
                day_option = (
                    minimum_money[max(i - 1, 0)] + costs[0]
                )  # if you buy 1-day ticket for travelling in day i
                week_option = (
                    minimum_money[max(i - 7, 0)] + costs[1]
                )  # buy 7-day ticket
                month_option = (
                    minimum_money[max(i - 30, 0)] + costs[2]
                )  # buy 30-day ticket
                minimum_money[i] = min(day_option, week_option, month_option)

        return minimum_money[-1]
