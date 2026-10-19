import numpy as np
#
# 1,100 observations, each with probability 0.5
p = np.full(1100, 0.5)
#
print("product:", np.prod(p))              # 0.0, the number got too small
print("sum of logs:", np.sum(np.log(p)))   # -762.46, perfectly fine
#
# the smallest positive number a float can hold, for comparison
print("float floor:", np.nextafter(0, 1))
