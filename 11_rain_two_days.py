import numpy as np
#
# 50% rain on Saturday, 50% on Sunday. Multiplying says 25% for both days,
# but only if the two days have nothing to do with each other.
print("if independent:", 0.5 * 0.5)
#
# a made-up town where rain likes to stay: after a rainy Saturday,
# Sunday rains 70% of the time; after a dry one, only 30%
rng = np.random.default_rng(7)
n = 2000
sat = rng.random(n) < 0.5
sun = np.where(sat, rng.random(n) < 0.7, rng.random(n) < 0.3)
print("Saturday rain share:", sat.mean())
print("Sunday rain share:", sun.mean())
print("both days:", (sat & sun).mean())     # about 0.35, not 0.25
