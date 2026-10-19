import numpy as np
#
# one week of step counts, Monday first
steps = np.array([6200, 8400, 4100, 9800, 7300, 11800, 3500])
#
# the sigma, written out the slow way
total = 0
for i in range(len(steps)):      # i walks 0..6, Python counts from zero
    total = total + steps[i]     # the "+" that the sigma is hiding
print("loop total:", total)
#
# the same sigma, the NumPy way
print("np.sum:", np.sum(steps))
#
# where the little 2 sits changes the answer
x = np.array([1, 2, 3])
print("sum of squares:", np.sum(x ** 2))    # 1 + 4 + 9 = 14
print("square of sum:", np.sum(x) ** 2)     # 6 squared = 36
