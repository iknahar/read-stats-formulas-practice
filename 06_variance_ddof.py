import numpy as np
import pandas as pd
#
steps = np.array([6200, 8400, 4100, 9800, 7300, 11800, 3500])
n = len(steps)
#
dev = steps - steps.mean()          # x_i minus x-bar, one per day
print("deviations:", dev)
print("they sum to:", dev.sum())    # always 0
#
ss = np.sum(dev ** 2)               # square, then add
print("divide by n:    ", ss / n)
print("divide by n - 1:", ss / (n - 1))
#
# the same seven numbers, two libraries, two defaults
print("np.var:        ", np.var(steps))              # ddof=0
print("pandas .var(): ", pd.Series(steps).var())     # ddof=1
print("np.var ddof=1: ", np.var(steps, ddof=1))      # now they agree
