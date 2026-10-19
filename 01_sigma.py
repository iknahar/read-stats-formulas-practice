import numpy as np
#
# one week of step counts, Monday first
steps = np.array([6200, 8400, 4100, 9800, 7300, 11800, 3500])
#
total = 0
for day in steps:          # visit each day once
    total = total + day    # the adding that the sigma sign hides
print("loop total:", total)              # 51100
#
print("np.sum:", np.sum(steps))          # the same sum in one line
print("np.mean:", np.mean(steps))        # the sum divided by 7, 7300.0
#
# where the little 2 sits changes the answer
x = np.array([1, 2, 3])
print("sum of squares:", np.sum(x ** 2))    # 1 + 4 + 9 = 14
print("square of sum:", np.sum(x) ** 2)     # 6 squared = 36
