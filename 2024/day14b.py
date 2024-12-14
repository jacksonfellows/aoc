import numpy as np

from day14a import calc_quad_counts

ii = np.arange(10_000)
scores = np.vectorize(lambda i: np.prod(calc_quad_counts(i)))(ii)
print(scores.argmin())
