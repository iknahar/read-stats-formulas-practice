import numpy as np
#
# what a phone's weekly report does: two averages and a percent change
this_week = np.array([6200, 8400, 4100, 9800, 7300, 11800, 3500])
last_week = np.array([9100, 7800, 8600, 10200, 6900, 12400, 3100])
#
a_this = this_week.mean()                  # add up, then divide
a_last = last_week.mean()
change = (a_this - a_last) / a_last        # subtract, then divide
print("this week:", a_this, "last week:", a_last)
print(f"change: {change:.1%}")             # -12.0%
