import numpy as np
#
steps = np.array([6200, 8400, 4100, 9800, 7300, 11800, 3500])
sleep = np.array([7.5, 6.0, 7.5, 7.0, 6.5, 6.5, 8.0])
#
dx = steps - steps.mean()                  # x_i minus x-bar
dy = sleep - sleep.mean()                  # y_i minus y-bar
top = np.sum(dx * dy)                      # the rectangles, added up
bottom = np.sqrt(np.sum(dx ** 2) * np.sum(dy ** 2))
r = top / bottom
print("r by hand:", round(r, 4))
print("np.corrcoef:", round(np.corrcoef(steps, sleep)[0, 1], 4))
#
# change units: covariance moves, r does not
print("cov in steps:", np.cov(steps, sleep)[0, 1])
print("cov in thousands:", np.cov(steps / 1000, sleep)[0, 1])
print("r in thousands:", round(np.corrcoef(steps / 1000, sleep)[0, 1], 4))
