import numpy as np
#
# a 1-unit bet on red, single-zero wheel: 18 red pockets out of 37
x = np.array([1, -1])                 # what you can win
p = np.array([18 / 37, 19 / 37])      # how likely each one is
#
expected = np.sum(x * p)              # E[X] = sum of x times p(x)
print("E[X]:", round(expected, 4))    # -0.027
#
# the long-run average of real (simulated) spins lands near it
rng = np.random.default_rng(17)
spins = np.where(rng.integers(0, 37, size=3000) < 18, 1, -1)
print("average after 3000 spins:", spins.mean())
#
# a fair die, the same recipe
faces = np.arange(1, 7)
print("E[die]:", np.sum(faces * np.full(6, 1 / 6)))   # 3.5
