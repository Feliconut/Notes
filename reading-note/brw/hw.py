from scipy.stats import binom
import numpy as np
# P(S_{n, p} >= k)
def binom_sf(n, p, k):
    return binom.sf(k - 1, n, p)
# # P(S_{n, p} <= k)
# def binom_cdf(n, p, k):
#     return binom.cdf(k, n, p)

# print(binom_sf(1000, 0.5, 520))
# res = []
# for n in range(1, 10001):
#     for p in [0.01 * i for i in range(1, 100)]:
#         # u = binom_sf(n, p, n*p + 0.01 * n)
#         l = binom_sf(n, p, n*p + 0.01 * n)
#         # if l ==0: print(n, p)
#         res.append(np.log(l) / n)
# print(min(res))

c = 0.151
# 2 exp(- c * n) = 0.01
n = int(np.log(0.005) / (-c)) + 1
print(n)