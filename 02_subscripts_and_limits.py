import numpy as np
#
steps = np.array([6200, 8400, 4100, 9800, 7300, 11800, 3500])
#
# maths counts i = 1..7, Python counts 0..6, so x_3 lives at steps[2]
print("x_3 (Wednesday):", steps[2])
#
# the limits on a sigma are a slice in disguise
print("mean of i = 1..7:", steps.mean())        # 7300.0
print("mean of i = 1..5:", steps[:5].mean())    # 7160.0, weekend dropped
#
# two subscripts: x_ij is row i, column j (weeks by days)
weeks = np.array([[6200, 8400, 4100, 9800, 7300, 11800, 3500],
                  [7700, 3400, 7900, 7900, 11100, 8100, 8500]])
print("x_23:", weeks[1, 2])                     # week 2, day 3
print("sum over j for week 2:", weeks[1].sum())
print("sum over i for each day:", weeks.sum(axis=0))
