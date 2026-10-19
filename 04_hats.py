import numpy as np
#
# the true line is y = 1 + 0.5 x, that 0.5 is beta (no hat)
rng = np.random.default_rng(8)
for sample in range(1, 6):
    x = rng.uniform(0.8, 9.2, 12)
    y = 1 + 0.5 * x + rng.normal(0, 0.9, 12)
    slope, intercept = np.polyfit(x, y, 1)   # beta-hat, from this sample
    print(f"sample {sample}: beta-hat = {slope:.2f}")
#
# p-hat: the share of heads you actually saw
flips = rng.integers(0, 2, size=50)
print("p-hat after 50 flips:", flips.mean())
