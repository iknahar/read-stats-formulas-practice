import numpy as np
#
steps = np.array([6200, 8400, 4100, 9800, 7300, 11800, 3500])
#
z = (steps - steps.mean()) / steps.std(ddof=1)   # subtract, then divide
print(np.round(z, 2))
print("Saturday is", round(z[5], 2), "spreads above the average day")
