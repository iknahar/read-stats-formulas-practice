import numpy as np
#
# true variance is 4. draw 4000 tiny samples of 5 and average each recipe
rng = np.random.default_rng(3)
x = rng.normal(0, 2.0, size=(4000, 5))
dev = x - x.mean(axis=1, keepdims=True)
ss = (dev ** 2).sum(axis=1)
#
print("average of ss / n:      ", (ss / 5).mean())    # about 3.2
print("average of ss / (n - 1):", (ss / 4).mean())    # about 4.0
