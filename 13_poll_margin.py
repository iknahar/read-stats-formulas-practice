import numpy as np
#
# a town where 52% truly support something (that is p, the truth)
p, n = 0.52, 1000
rng = np.random.default_rng(2)
#
# forty polls, each asking 1,000 people (each result is a p-hat)
p_hats = rng.binomial(n, p, size=40) / n
margin = 1.96 * np.sqrt(p * (1 - p) / n)   # the famous "plus or minus 3"
print("margin of error:", round(margin, 3))
print("first five polls:", p_hats[:5])
inside = np.abs(p_hats - p) <= margin
print("polls inside the margin:", inside.sum(), "of", len(p_hats))
