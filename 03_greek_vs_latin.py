import numpy as np
#
# pretend we know the truth: mu = 7300 steps, sigma = 2600
rng = np.random.default_rng(6)
mu, sigma = 7300, 2600
#
# forty imaginary weeks, seven days each, one x-bar per week
weeks = rng.normal(mu, sigma, size=(40, 7))
xbars = weeks.mean(axis=1)
#
print("true mu:", mu)
print("first five x-bars:", np.round(xbars[:5]))
print("smallest and largest x-bar:", round(xbars.min()), round(xbars.max()))
print("average of all forty x-bars:", round(xbars.mean()))
